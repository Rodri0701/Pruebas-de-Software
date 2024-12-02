# Pruebas automatizadas en front end "Mercado Libre"


# DESCRIPCIÓN:  
Pruebas automatizadas para verificar diversas funciones de la pagina *"Mercado Libre"*

# Instalación

    Clona el repositorio: git clone https://github.com/Rodri0701/SF_Almacen.git


1. Instalar Node.js

Antes de instalar Playwright, asegúrate de tener Node.js instalado en tu sistema.

    Descarga e instala desde la página oficial de Node.js.
    Verifica la instalación ejecutando:

    node -v
    npm -v

2. Crear un Proyecto Node.js

Si aún no tienes un proyecto configurado, crea uno:

    Abre tu terminal y navega al directorio de tu proyecto.
    Ejecuta:

    npm init -y

    Esto creará un archivo package.json.

3. Instalar Playwright

Para instalar Playwright, usa el siguiente comando:

npm install playwright

Este comando descargará Playwright junto con los navegadores compatibles (Chromium, Firefox, y WebKit).

Si solo necesitas navegadores específicos, puedes usar:

*Solo para Chromium*
npm install playwright-chromium

*Solo para Firefox*
npm install playwright-firefox

*Solo para WebKit*
npm install playwright-webkit

4. Configurar Playwright para Pruebas

Para generar una configuración inicial de Playwright, ejecuta:

npx playwright install

Esto asegurará que todos los navegadores necesarios estén instalados.

Si estás configurando un entorno de pruebas, puedes iniciar con:

npx playwright test init

Esto creará una estructura base para pruebas (como una carpeta tests y un archivo de configuración playwright.config.ts).
5. Escribir tu Primera Prueba

Crea un archivo de prueba, por ejemplo, tests/example.spec.ts

6. Ejecutar las Pruebas

Corre las pruebas con:

npx playwright test
