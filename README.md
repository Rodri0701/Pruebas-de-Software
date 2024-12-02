# Pruebas Automatizadas en Front End "Mercado Libre"

## DESCRIPCIÓN
Pruebas automatizadas para verificar diversas funciones de la página *"Mercado Libre"*.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Rodri0701/SF_Almacen.git
    ```

2. Instalar Node.js

   Antes de instalar Playwright, asegúrate de tener Node.js instalado en tu sistema.

   - Descarga e instala desde la página oficial de Node.js.
   - Verifica la instalación ejecutando:
     ```bash
     node -v
     npm -v
     ```

3. Crear un Proyecto Node.js

   Si aún no tienes un proyecto configurado, crea uno:

   - Abre tu terminal y navega al directorio de tu proyecto.
   - Ejecuta:
     ```bash
     npm init -y
     ```
   Esto creará un archivo `package.json`.

4. Instalar Playwright

   Para instalar Playwright, usa el siguiente comando:
   ```bash
   npm install playwright
   ```
   Este comando descargará Playwright junto con los navegadores compatibles (Chromium, Firefox, y WebKit).

Si solo necesitas navegadores específicos, puedes usar:

- **Solo para Chromium**
  ```bash
  npm install playwright-chromium
- **Solo para Firefox**
  ```bash
    npm install playwright-firefox
  ```
- **Solo para Webkit**
  ```bash
    npm install playwright-webkit
  ```

5. Configurar Playwright para Pruebas

Para generar una configuración inicial de Playwright, ejecuta:
```bash
npx playwright install
```
Esto asegurará que todos los navegadores necesarios estén instalados.

6. Ejecutar las Pruebas

Corre las pruebas con:
```bash
npx playwright test
```
