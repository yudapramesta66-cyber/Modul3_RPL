from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController

class AuthController:
    def __init__(self, model=None, view=None):
        self.model = model if model else UserModel()
        self.view = view if view else LoginView()

        self.view.btn_login.configure(command=self.proses_login)

    def proses_login(self):
        username, password = self.view.get_credentials()
        if not username or not password:
            self.view.show_error("Username dan password wajib diisi!")
            return

        user = self.model.verify_user(username, password)
        if user:
            self.view.show_info(f"Selamat datang, {user['username']} (Role: {user['role']})!")
            self.view.destroy()
            buku_app = BukuController(user_role=user["role"])
            buku_app.run()
        else:
            self.view.show_error("Username atau password salah!")

    def run(self):
        self.view.mainloop()