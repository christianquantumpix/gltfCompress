import os
import tkinter
#from tkinter import filedialog, Listbox
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.input_files = []

        # configure window
        self.title("gltfpack mesh compressor")
        self.geometry(f"{600}x{300}")
        self.resizable(False, False)

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.select_input_folder = customtkinter.CTkButton(
            master=self, 
            text="Open Folder...", 
            command=self.load_file_list
        )
        self.select_input_folder.place(relx=.1, rely=.1, anchor=tkinter.NW)

        self.select_output_folder = customtkinter.CTkButton(
            master=self, 
            text="Output Folder...", 
            command=self.load_file_list,
            state="disabled"
        )
        self.select_output_folder.place(relx=.1, rely=.2, anchor=tkinter.NW)

        self.select_output_folder = customtkinter.CTkButton(
            master=self, 
            text="Convert All", 
            command=self.convert
        )
        self.select_output_folder.place(relx=.1, rely=.3, anchor=tkinter.NW)

        self.status_label = customtkinter.CTkLabel(
            self, 
            text="Ready to rock and roll!", 
            font=customtkinter.CTkFont(size=14, weight="bold"))
        self.status_label.place(relx=.1, rely=.4, anchor=tkinter.NW)

        self.file_list = tkinter.Listbox(
            self,
            width=48
        )
        self.file_list.place(relx=.5, rely=.1, anchor=tkinter.NW)

    def convert(self):
        current_directory = os.getcwd()
        for input_file in self.input_files:
            os.system(current_directory + "/bin/gltfpack.exe -i " + input_file + " -o " + input_file + " -cc -tc -kn -km -ke")
        self.status_label.configure(text="Conversion completed!")

    def load_file_list(self):
        input_directory = tkinter.filedialog.askdirectory()

        self.input_files.clear()
        self.file_list.delete(0, tkinter.END)

        for root, dirs, files in os.walk(input_directory):
            for file in files:
                if file.endswith(".gltf") or file.endswith(".glb"):
                    #file_path = os.path.join(root, file)
                    file_path = root + "/" + file
                    relative_path = file_path.replace(input_directory, "")

                    self.input_files.append(file_path)
                    self.file_list.insert(tkinter.END, relative_path[1:])

if __name__ == "__main__":
    app = App()
    app.mainloop()
