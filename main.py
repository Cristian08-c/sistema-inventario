import utils.jwt_handler_util as jwt_util
import backend
import frontend

# 🔹 Variables globales para manejar las ventanas activas
login_app = None
home_app = None


def iniciar_aplicacion():
    global login_app, home_app

    token = jwt_util.obtener_token()

    if token:
        payload = jwt_util.verify_token(token)
        if payload:
            print("Sesión activa detectada. Bienvenido de nuevo,", payload.get("sub", "usuario"))
            mostrar_home()
            return
        else:
            print("Token expirado o inválido. Debes iniciar sesión de nuevo.")
            mostrar_pantalla_login()
    else:
        print("No hay sesión activa. Por favor, inicia sesión.")
        mostrar_pantalla_login()


def mostrar_pantalla_login():
    """Abre la ventana de login"""
    global login_app
    login_app = frontend.AuthenticateApp()
    login_app.mainloop()


def procesar_login(username, password):
    """Valida las credenciales y abre la app principal"""
    global login_app
    auth = backend.Authentication(username, password)
    token = auth.login()

    if token:
        from utils.jwt_handler_util import guardar_token
        guardar_token(token)
        print("Sesión iniciada. Token guardado.")
        cerrar_login()  # 🔹 Cerrar ventana de login
        mostrar_home()
    else:
        print("Error: No se pudo iniciar sesión.")


def mostrar_home():
    """Abre la ventana principal"""
    global home_app
    home_app = frontend.HomeApp()
    home_app.mainloop()


def cerrar_login():
    """Cierra la ventana de login si está abierta"""
    global login_app
    if login_app:
        try:
            login_app.destroy()
            print("Ventana de login cerrada.")
        except Exception as e:
            print("Error al cerrar login:", e)
        login_app = None


def cerrar_sesion():
    """Cierra sesión y vuelve a la pantalla de login"""
    global home_app
    jwt_util.borrar_token()
    print("Sesión cerrada correctamente.")
    if home_app:
        try:
            home_app.destroy()
        except Exception as e:
            print("Error al cerrar HomeApp:", e)
        home_app = None
    mostrar_pantalla_login()


if __name__ == "__main__":
    iniciar_aplicacion()


