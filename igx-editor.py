import tkinter as tk
from tkinter import filedialog, ttk
import xml.etree.ElementTree as ET
from igEnums import *  # Import all enums from igEnums
from enum import Enum

class IGXViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("IGX Viewer")
        self.root.geometry("800x600")

        self.objects = []
        self.current_object_index = None
        self.var_entries = []
        self.tree = None

        self.object_frame = tk.Frame(root)
        self.object_frame.pack(side="left", fill="both", expand=True)

        self.object_list = tk.Listbox(self.object_frame, selectmode="SINGLE")
        self.object_list.pack(side="left", fill="both", expand=True)
        self.object_list.bind("<<ListboxSelect>>", self.select_object)

        self.scrollbar = tk.Scrollbar(self.object_frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.object_list.yview)

        self.var_frame = tk.Frame(root)
        self.var_frame.pack(side="right", fill="both", expand=True)

        self.load_button = tk.Button(root, text="Load IGX File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Changes", command=self.save_changes)
        self.save_button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Select igXml File",
            filetypes=[("igXml Files", "*.igx"), ("All Files", "*.*")]
        )
        if file_path:
            self.parse_igx(file_path)

    def parse_igx(self, file_path):
        self.objects.clear()
        self.object_list.delete(0, tk.END)

        self.tree = ET.parse(file_path)
        root = self.tree.getroot()
        for obj in root.findall(".//object"):
            obj_name = obj.get("refname")
            print(f"Object found: {obj_name}")  # Debug print for object found
            vars_list = obj.findall(".//var[@value]")
            self.objects.append(obj)  # Always append, even if no vars
            self.object_list.insert(tk.END, obj_name)

    def display_vars(self):
        self.clear_vars()

        if self.current_object_index is not None:
            selected_object = self.objects[self.current_object_index]
            vars_list = selected_object.findall(".//var[@value]")
            for var_index, var in enumerate(vars_list):
                var_name = var.get("name", "Unknown")
                var_value = var.get("value", "Unknown")
                print(f"Variable found: {var_name} with value: {var_value}")  # Debug print for var found

                label = tk.Label(self.var_frame, text=f"{var_name}:", padx=10, pady=5)
                label.grid(row=var_index, column=0, sticky="w")

                # Check if the value is a boolean
                if var_value in ["True", "False", "true", "false"]:
                    var_value_bool = var_value.lower() == "true"
                    var_entry = tk.BooleanVar(value=var_value_bool)
                    checkbutton = tk.Checkbutton(self.var_frame, variable=var_entry)
                    checkbutton.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)
                else:
                    enum_found = False
                    for enum_class_name, enum_class in globals().items():
                        if isinstance(enum_class, type) and issubclass(enum_class, Enum):
                            if var_value in [e.value for e in enum_class]:
                                print(f"Value '{var_value}' matches enum '{enum_class_name}'")  # Debug print for enum match
                                var_entry = ttk.Combobox(self.var_frame, values=[e.value for e in enum_class], width=40)
                                var_entry.set(var_value)
                                var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                                self.var_entries.append(var_entry)
                                enum_found = True
                                break 

                    if not enum_found:
                        # Default value, this sometimes breaks but I won't worry about it for now.
                        var_entry = tk.Entry(self.var_frame, width=30)
                        var_entry.insert(0, var_value)
                        var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                        self.var_entries.append(var_entry)

    def clear_vars(self):
        for widget in self.var_frame.winfo_children():
            widget.destroy()
        self.var_entries.clear()

    def select_object(self, event):
        selection = self.object_list.curselection()
        if selection:
            self.current_object_index = selection[0]
            self.display_vars()

    def save_changes(self):
        if self.current_object_index is None:
            return  # No object selected

        selected_object = self.objects[self.current_object_index]
        vars_list = selected_object.findall(".//var[@value]")

        for var_index, var in enumerate(vars_list):
            if var_index < len(self.var_entries):  # Ensure the variable exists
                entry = self.var_entries[var_index]
                var.set("value", entry.get())  # Save the value

        # Saving changes back to the IGX file
        file_path = filedialog.asksaveasfilename(
            title="Save IGX File",
            defaultextension=".igx",
            filetypes=[("igXml Files", "*.igx"), ("MUA Files", "*.mua"), ("All Files", "*.*")]
        )
        if file_path:
            # Use the original tree to save the updated igXml
            self.tree.write(file_path, encoding="utf-8", xml_declaration=False)
            print("Changes saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = IGXViewer(root)
    root.mainloop()
