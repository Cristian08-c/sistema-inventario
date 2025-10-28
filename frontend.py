import customtkinter as CTK
import backend
import time
import threading

class AuthenticateApp(CTK.CTk):
    def __init__(self):
        super().__init__()

        self.title("Authentication")

        window_width = 600
        window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.resizable(False, False)

        self.log_in()

    def safe_fade(self, window, start, end, step, callback=None):
        def _fade():
            try:
                alpha = start
                while (alpha > end if start > end else alpha < end):
                    window.attributes("-alpha", alpha / 100)
                    alpha += step
                    time.sleep(0.02)
                window.attributes("-alpha", end / 100)
                if callback:
                    window.after(0, callback)
            except Exception:
                pass 
        threading.Thread(target=_fade, daemon=True).start()

    def sign_up(self):
        self.safe_fade(self, 100, 0, -5, callback=lambda: self.open_sign_up())

    def open_sign_up(self):
        try:
            self.destroy()
        except:
            pass

        sign_up_window = CTK.CTk()
        sign_up_window.title("Sign Up")

        window_width = 600
        window_height = 600

        screen_width = sign_up_window.winfo_screenwidth()
        screen_height = sign_up_window.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        sign_up_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        sign_up_window.resizable(False, False)
        sign_up_window.attributes("-alpha", 0)

        self.safe_fade(sign_up_window, 0, 100, 5)

       
        label = CTK.CTkLabel(master=sign_up_window, text="ColMarket", font=("Segoe UI", 30, "bold"))
        label.grid(pady=40)

        frame = CTK.CTkFrame(master=sign_up_window, width=500, height=450)
        frame.grid_propagate(False)
        frame.grid(padx=50, pady=1)

        label_signup = CTK.CTkLabel(master=frame, text="Create Your Account", font=("Segoe UI", 24, "bold"))
        label_signup.grid(pady=30, padx=120)

        entry_username = CTK.CTkEntry(master=frame, placeholder_text="Username", font=("Segoe UI", 18), width=400, height=50)
        entry_username.grid(pady=20, padx=10)
        entry_password = CTK.CTkEntry(master=frame, placeholder_text="Password", font=("Segoe UI", 18), width=400, height=50, show="*")
        entry_password.grid(pady=20, padx=10)

        button_signup = CTK.CTkButton(
            master=frame,
            text="Sign Up",
            font=("Segoe UI", 24, "bold"),
            width=400,
            height=50,
            fg_color="#1f6aa5",
            hover_color="#1665a2",
            cursor="hand2",
            command=lambda: (
            backend.Authentication(
            entry_username.get(),
            entry_password.get()
            ).signup()
            )
        )
        button_signup.grid(pady=30, padx=10)

    
        label_login = CTK.CTkLabel(
            master=frame, text="Already have an account? Login",
            font=("Segoe UI", 18, "bold"), cursor="hand2"
        )
        label_login.grid(pady=1, padx=100)

        label_login.bind("<Enter>", lambda e: label_login.configure(text_color="#1f6aa5"))
        label_login.bind("<Leave>", lambda e: label_login.configure(text_color="white"))
        label_login.bind("<Button-1>", lambda e: self.back_to_login(sign_up_window))

        sign_up_window.mainloop()

    def back_to_login(self, sign_up_window):
        self.safe_fade(sign_up_window, 100, 0, -5, callback=lambda: self.reopen_login(sign_up_window))

    def reopen_login(self, sign_up_window):
        try:
            sign_up_window.destroy()
        except:
            pass
        app = AuthenticateApp()
        app.attributes("-alpha", 0)
        self.safe_fade(app, 0, 100, 5)
        app.mainloop()

    def log_in(self):
        label = CTK.CTkLabel(master=self, text="ColMarket", font=("Segoe UI", 30, "bold"))
        label.grid(pady=40)

        frame = CTK.CTkFrame(master=self, width=500, height=450)
        frame.grid_propagate(False)
        frame.grid(padx=50, pady=1)

        label_login = CTK.CTkLabel(master=frame, text="Login to Your Account", font=("Segoe UI", 24, "bold"))
        label_login.grid(pady=30, padx=120)

        entry_username = CTK.CTkEntry(master=frame, placeholder_text="Username", font=("Segoe UI", 18), width=400, height=50)
        entry_username.grid(pady=20, padx=10)
        entry_password = CTK.CTkEntry(master=frame, placeholder_text="Password", font=("Segoe UI", 18), width=400, height=50, show="*")
        entry_password.grid(pady=20, padx=10)

        button_login = CTK.CTkButton(
            master=frame,
            text="Login",
            font=("Segoe UI", 24, "bold"),
            width=400,
            height=50,
            fg_color="#1f6aa5",
            hover_color="#1665a2",
            cursor="hand2",
            command=lambda:(
            backend.Authentication(
            entry_username.get(),
            entry_password.get()
            ).login()
          )
        )

        button_login.grid(pady=30, padx=10)

        label_signup = CTK.CTkLabel(
            master=frame, text="Don't have an account? Sign Up",
            font=("Segoe UI", 18, "bold"), cursor="hand2"
        )
        label_signup.grid(pady=10, padx=100)

        label_signup.bind("<Button-1>", lambda e: self.sign_up())
        label_signup.bind("<Enter>", lambda e: label_signup.configure(text_color="#1f6aa5"))
        label_signup.bind("<Leave>", lambda e: label_signup.configure(text_color="white"))

if __name__ == "__main__":
    AuthenticateApp().mainloop()
