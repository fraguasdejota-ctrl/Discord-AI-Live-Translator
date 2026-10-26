# 🎧 TraductorDiscordPro — Real-Time AI Voice Overlay

![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-0078D6?style=for-the-badge&logo=windows)
![Android](https://img.shields.io/badge/Android-In%20Development-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python)
![Cython](https://img.shields.io/badge/Compiled-Cython%20C--Extension%20(.pyd)-F34B7D?style=for-the-badge&logo=c)
![UI](https://img.shields.io/badge/UI-PyQt6%20Frameless-41CD52?style=for-the-badge&logo=qt)
![AI](https://img.shields.io/badge/Inference-Groq%20LPU%20%2F%20Whisper-FF6F00?style=for-the-badge)

**TraductorDiscordPro** es una herramienta de escritorio de baja latencia para Windows que captura el flujo de audio del sistema (Discord, videojuegos, llamadas o streaming) mediante **WASAPI Loopback** y genera subtítulos traducidos en tiempo real sobre una interfaz *overlay* transparente con soporte *Click-Through*.

📥 **[Descargar Ejecutable Gratuito (.exe) en la sección Releases](../../releases)**

---

## 🏗️ Arquitectura e Ingeniería del Software

Este proyecto implementa una **arquitectura de distribución híbrida (Python + C Nativo)** orientada a proteger la lógica de negocio y optimizar el rendimiento de procesamiento de buffers de audio:

1. **Captura de Audio en Bucle Cerrado (WASAPI Loopback):** Captura directa del flujo de salida de la tarjeta de sonido sin necesidad de cables virtuales externos (VB-Cable), procesando bloques PCM en memoria mediante hilos asíncronos (`daemon threads`).
2. **Inferencia de Ultra-Baja Latencia:** Transcripción y traducción acelerada mediante API sobre unidad de procesamiento de lenguaje (Groq LPU), gestionando credenciales de usuario de forma segura y persistente en el registro del sistema (`QSettings`).
3. **Interfaz Gráfica No Intrusiva (PyQt6):**
   * Ventana transparente sin bordes (`FramelessWindowHint` + `WindowStaysOnTopHint`).
   * **Modo Click-Through Nativo:** Inyección de banderas `WindowTransparentForInput` para permitir hacer clic a través de los subtítulos mientras se juega.
   * **Integración en System Tray:** Control completo desde la bandeja del sistema de Windows para bloquear/desbloquear la posición, pausar o cambiar la API Key en caliente.
4. **Protección de Propiedad Intelectual (Cython + PyInstaller):**
   * El motor principal (`traductor_core`) se transpila a código **C nativo** y se compila en una librería dinámica de Windows (`.pyd`) mediante `MSVC`, previniendo la descompilación e ingeniería inversa del *bytecode*.
   * Un lanzador desacoplado (`main.py`) gestiona la declaración explícita del árbol de dependencias para el empaquetador estático.

---

## 🚀 Instalación y Uso (Versión Usuario)

No requiere instalar Python ni dependencias adicionales:

1. Ve a la sección de **[Releases](../../releases)** de este repositorio y descarga **`TraductorDiscordPro.exe`**.
2. Ejecuta la aplicación. En el primer inicio, introduce tu **API Key gratuita de Groq** (puedes cambiarla en cualquier momento desde el botón `🔑 API Key`).
3. Coloca el overlay donde prefieras usando el botón **`✢ Mantén clic aquí para Mover`**.
4. Pulsa **`🔒 Fijar (Click-Through)`** para bloquear los subtítulos y que los clics del ratón atraviesen la ventana hacia tu juego o Discord.
5. Para volver a moverlo, pausarlo o cerrarlo, haz clic derecho en el **icono verde de la bandeja del sistema (junto al reloj de Windows)**.

---

## 🗺️ Hoja de Ruta (Roadmap de Desarrollo)

**TraductorDiscordPro** es un proyecto en evolución continua bajo un flujo de desarrollo *PC-First*. Las próximas expansiones del ecosistema incluyen:

- [x] **v1.0.0 (Windows x64):** Lanzamiento estable con captura WASAPI Loopback, inferencia Groq LPU, modo *Click-Through* y núcleo compilado en C nativo (`.pyd`).
- [ ] **v1.1.0 (Windows x64):** Selector de idiomas de origen/destino en tiempo real y personalización de fuentes/opacidad desde la bandeja del sistema.
- [ ] **📱 Versión Nativa para Android (`.apk`) *(En desarrollo)*:** Portado de la arquitectura a dispositivos móviles mediante `AudioPlaybackCapture API`, ventana flotante nativa (`SYSTEM_ALERT_WINDOW`) y núcleo lógico compilado en C++ mediante **Android NDK (`.so`)**.
- [ ] **🌐 Portal Web Oficial *(Próximamente)*:** Lanzamiento de *Landing Page* centralizada con descargas directas multiplataforma (Windows & Android), documentación interactiva y notas de parche.

---

## 🔒 Nota sobre el Código Fuente (Open Showcase)

La herramienta se distribuye de forma **100% gratuita** para la comunidad a través del binario precompilado. Por motivos de protección de propiedad intelectual y seguridad en la arquitectura de prompts y concurrencia, el módulo central (`traductor_core.pyd`) se distribuye compilado en binario C nativo. En este repositorio se incluyen los scripts de arquitectura de lanzamiento (`main.py`) y configuración de compilación (`setup.py`) con fines demostrativos de ingeniería de empaquetado.

---

## ☕ Apoya el Proyecto (Donaciones)

Si la herramienta te resulta útil en tus partidas, llamadas o *streams* y quieres apoyar el desarrollo de la versión para Android y las futuras actualizaciones:

[![PayPal](https://img.shields.io/badge/Donar_con-PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)] (https://paypal.me/JuanFraguas)
