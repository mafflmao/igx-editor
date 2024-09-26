import tkinter as tk
from tkinter import filedialog, simpledialog, ttk
import xml.etree.ElementTree as ET
from igEnums.CriticalType import CriticalType
from igEnums.ECollectibleType import ECollectibleType
from igEnums.ECollectibleWorldModifierCategory import ECollectibleWorldModifierCategory
from igEnums.EEntityTeam import EEntityTeam
from igEnums.EQueryFilterType import EQueryFilterType
from igEnums.EQuerySortMode import EQuerySortMode
from igEnums.XBUTTON import XBUTTON
from igEnums.EPointOfInterest import EPointOfInterest
from igEnums.EStructure import EStructure
from igEnums.EffectKillTypes import EffectKillTypes
from igEnums.EFlags import EFlags
from igEnums.CriticalType import CriticalType
from igEnums.EPhysicalEntityDataFlags import EPhysicalEntityDataFlags

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
        self.clear_vars()

        if self.current_object_index is not None:
            selected_object = self.objects[self.current_object_index]
            vars_list = selected_object.findall(".//var[@value]")
            for var_index, var in enumerate(vars_list):
                var_name = var.get("name", "Unknown")
                var_value = var.get("value", "Unknown")

                label = tk.Label(self.var_frame, text=f"{var_name}:", padx=10, pady=5)
                label.grid(row=var_index, column=0, sticky="w")

                # Boolean Values
                if var_value in ["True", "False", "true", "false"]:
                    var_value_bool = var_value.lower() == "true"
                    var_entry = tk.BooleanVar(value=var_value_bool)
                    checkbutton = tk.Checkbutton(self.var_frame, variable=var_entry)
                    checkbutton.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(checkbutton)

                # igEnums.ECollectibleType
                elif var_name in ["_collectibleType", "CollectibleType"]:
                    var_entry = ttk.Combobox(self.var_frame, values=[e.value for e in ECollectibleType])
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

                # igEnums.ECollectibleWorldModifierCategory
                elif var_name in ["_worldModifierCategory", "WorldModifierCategory"]:
                    var_entry = ttk.Combobox(self.var_frame, values=[e.value for e in ECollectibleWorldModifierCategory])
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

                # igEnums.EEntityTeam
                elif var_name in ["_team", "Team"]:
                    var_entry = ttk.Combobox(self.var_frame, values=[e.value for e in EEntityTeam])
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

                # igEnums.XBUTTON
                elif var_name in ["_button", "Button"]:
                    button_options = [e.value for e in XBUTTON]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)
                    
                # igEnums.EStructure
                elif var_name in ["_structure", "Structure"]:
                    button_options = [e.value for e in EStructure]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

		        # igEnums.EPointOfInterest
                elif var_name in ["_type", "Type"]:
                    button_options = [e.value for e in EPointOfInterest]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)
                    
                # igEnums.EffectKillTypes
                elif var_name in ["_killTypeOnEnd", "KillTypeOnEnd", "_killType", "KillType"]:
                    button_options = [e.value for e in EffectKillTypes]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

                elif var_name in ["_sortMode", "SortMode", "SortType", "_sortType"]:
                    button_options = [e.value for e in EQuerySortMode]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

                elif var_name in ["_filterMode", "FilterMode", "FilterType", "_filterType"]:
                    button_options = [e.value for e in EQueryFilterType]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)
                    
                elif var_name in ["_flag", "Flag", "_flags", "Flags"]:
                    button_options = [e.value for e in EFlags]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)
                    
                elif var_name in ["_critical", "Critical"]:
                    button_options = [e.value for e in CriticalType]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)
                    
                elif var_name in ["_physicalEntityFlags"]:
                    button_options = [e.value for e in EPhysicalEntityDataFlags]
                    var_entry = ttk.Combobox(self.var_frame, values=button_options)
                    var_entry.set(var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

                # Default string, might mess up other stuff but unsure at the moment
                else:
                    var_entry = tk.Entry(self.var_frame, width=20)
                    var_entry.insert(0, var_value)
                    var_entry.grid(row=var_index, column=1, padx=5, pady=5, sticky="e")
                    self.var_entries.append(var_entry)

    def select_object(self, event):
        selected_index = self.object_list.curselection()
        if selected_index:
            self.current_object_index = selected_index[0]
            self.display_vars()
        else:
            self.current_object_index = None
            self.clear_vars()

    def clear_vars(self):
        for entry in self.var_entries:
            if isinstance(entry, tk.Entry) or isinstance(entry, ttk.Combobox):
                entry.destroy()  
        self.var_entries.clear()  

        for label in self.var_frame.winfo_children():
            label.destroy()

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
            with open(save_file_path, "wb") as f:
                tree.write(f)

            print("Changes saved successfully!")

def main():
    root = tk.Tk()
    igx_viewer = IGXViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
