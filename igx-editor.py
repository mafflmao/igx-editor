import tkinter as tk
from tkinter import filedialog
from tkinter import OptionMenu
import xml.etree.ElementTree as ET

class IGXViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("IGX Viewer")
        self.root.geometry("800x600")

        self.objects = []
        self.current_object_index = None
        self.var_entries = []

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
            title="Select IGX File",
            filetypes=[("IGX Files", "*.igx"), ("All Files", "*.*")]
        )
        if file_path:
            self.parse_igx(file_path)

    def parse_igx(self, file_path):
        self.objects.clear()
        self.object_list.delete(0, tk.END)

        root = ET.parse(file_path).getroot()
        for obj in root.findall(".//object"):
            obj_name = obj.get("refname")
            vars_list = obj.findall(".//var[@value]")
            if vars_list:
                self.objects.append(obj)
                self.object_list.insert(tk.END, obj_name)

    def display_vars(self):
        for entry in self.var_entries:
            entry.destroy()
        self.var_entries.clear()

        if self.current_object_index is not None:
            selected_object = self.objects[self.current_object_index]
            vars_list = selected_object.findall(".//var[@value]")
            for var_index, var in enumerate(vars_list):
                var_name = var.get("name", "Unknown")
                var_value = var.get("value", "Unknown")

                label = tk.Label(self.var_frame, text=f"{var_name}:", padx=10, pady=5)
                label.grid(row=var_index, column=0, sticky="w")

                if var_value == "eET_Hero":
                    var_dropdown = tk.StringVar(self.root)
                    var_dropdown.set("eET_Hero")
                    dropdown_menu = OptionMenu(self.var_frame, var_dropdown, "eET_None", "eET_Hero", "eET_Enemy", "eET_AltEnemy")
                    dropdown_menu.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_dropdown)
                else:
                    var_entry = tk.Entry(self.var_frame, width=20)
                    var_entry.insert(0, var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

    def select_object(self, event):
        selected_index = self.object_list.curselection()
        if selected_index:
            self.current_object_index = selected_index[0]
            self.clear_vars()  
            self.display_vars()  
        else:
            self.current_object_index = None
            self.clear_vars()  

    def clear_vars(self):
        for entry in self.var_entries:
            entry.destroy()  
        self.var_entries.clear()  

    def save_changes(self):
        if not self.objects:
            return

        save_file_path = filedialog.asksaveasfilename(
            title="Save IGX File",
            filetypes=[("IGX Files", "*.igx"), ("All Files", "*.*")]
        )
        if save_file_path:
            root = ET.Element("igx")
            for obj in self.objects:
                root.append(obj)

            tree = ET.ElementTree(root)
            with open(save_file_path, "w") as f:
                f.write("<igx>\n")
                for obj in root:
                    f.write("\t" + ET.tostring(obj, encoding="unicode").strip() + "\n")
                f.write("</igx>\n")

            print("Changes saved successfully! yay!")

def main():
    root = tk.Tk()
    igx_viewer = IGXViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()