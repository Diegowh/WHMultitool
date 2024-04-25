from threading import Thread, Event
import time
import tkinter as tk
import keyboard
import pyautogui


class AutoSim(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.autosim_running = False
        self.autosim_thread = None
        self.ignore_next_stop = False  # error with the code duel hitting the toggle for some reason
        self.autosim_last_click_time = time.time() - 1
        self.autosim_running = False  # This will track the running state internally, not in config
        keyboard.register_hotkey('f6', self.toggle_autosim, suppress=True)
        self.autosim_label = None
        
        self.text_input = tk.StringVar()
        self.title("Wallhack el mejor UwU")
        self.geometry("300x200")
        self.resizable(False, False)
        self.init_gui()

    def init_gui(self) :
        """
        Initialize the GUI components.
        """
        instructions_label = tk.Label(self, text="F6 - Toggle autosim")
        instructions_label.pack(padx=20, pady=20)
        self.autosim_label = instructions_label
        
        map_num_label = tk.Label(self, text="Map number:")
        map_num_label.pack()

        map_num_entry = tk.Entry(self, textvariable=self.text_input)
        map_num_entry.pack(padx=10, pady=10)

    def start_autosim(self):
        if not self.autosim_running:
            self.autosim_running = True
            self.autosim_thread = Thread(target=self.run_auto_sim)
            self.autosim_thread.start()
            print("Auto-sim started")

    def stop_autosim(self):
        if self.autosim_running:
            self.autosim_running = False
            if self.autosim_thread is not None:
                self.autosim_thread.join()
            print("Auto-sim stopped")
    
    def run_auto_sim(self):
        try:
            while self.autosim_running:
                map_number = self.text_input.get()
                self.autosim_routine(map_number)
            print("Auto-sim stopping")
        except Exception as e:
            print(f"Error: {e}")
            self.autosim_running = False

    def toggle_autosim(self, event=None):
        if self.autosim_running:
            self.stop_autosim()
        else:
            self.start_autosim()

    def get_screen_resolution(self):
        width, height = pyautogui.size()
        return width, height
    
    def move_and_click(self, x, y, sleep_time=0.5):
        screen_w, screen_h = self.get_screen_resolution()
        # Default values are for 1920x1080 resolution, so we need to check if the resolution is different
        if screen_w != 1920 or screen_h != 1080:
            x *= screen_w / 1920
            y *= screen_h / 1080
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(sleep_time)
    
    # def debug_function(self, map_number):
    #     while self.autosim_running:
    #         print(f"function running with map number: {map_number}")
    #         time.sleep(1)
        
    def autosim_routine(self, map_number):
        while self.autosim_running:
            self.move_and_click(934, 858)  # Press middle button on the start screen
            self.move_and_click(705, 523)  # Press Join Game button
            self.move_and_click(1670, 200)  # Click on the map search bar
            pyautogui.write(map_number)
            pyautogui.press('enter')
            time.sleep(0.5)  # Wait for the map list to load
            self.move_and_click(930, 335)  # Click on the first map in the list
            self.move_and_click(1700, 945, 3)  # Click Join and wait 3 seconds for the mod selection screen to load
            self.move_and_click(340, 930)  # Click Join
            time.sleep(10)  # Delay to allow the Server full message to appear
            pyautogui.press('esc')
            time.sleep(0.5)
            self.move_and_click(170, 880)
            self.move_and_click(964, 964)
            
app = AutoSim()
app.mainloop()