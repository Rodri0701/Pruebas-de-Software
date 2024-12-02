import { test, expect } from '@playwright/test';


test.describe('Pruebas de las pruebas', () => {
  test('test 1', async ({ page }) => {
    await page.goto('https://www.amazon.com.mx/');
    await expect(page).toHaveTitle(/Amazon.com.mx/);

    const searchInput = page.locator("input[id='twotabsearchtextbox']");
    await expect(searchInput).toBeVisible();

    await searchInput.fill('Xbox');
    await page.keyboard.press('Enter');
    await expect(page).toHaveTitle(/Amazon.com.mx : *xbox/i);

    const searchResultHighlight = page.locator("span[class='a-color-state a-text-bold']");
    await expect(searchResultHighlight).toContainText('Xbox');
    await page.pause();
  });
  test("Laptops y accesorios", async ({ page }) => {
    await page.goto('https://listado.mercadolibre.com.mx/computadoras#D[A:computadoras]/');
    await page.pause();

    await page.locator('span[class="ui-search-filter-name"]:has-text("Laptops y Accesorios")').click();
    await page.pause();

    const categorias = page.locator("span[itemprop='name']:has-text('Laptops y Accesorios')");
    await expect(categorias).toBeVisible();
    await page.pause();
  });
  test("PC de Escritorio", async ({ page }) => {
    await page.goto('https://www.mercadolibre.com.mx/');
    await expect(page).toHaveTitle(/Mercado Libre México - *Envíos Gratis en el día/i);
    await page.pause();

    const navegador = page.locator("input[class='nav-search-input']");
    await expect(navegador).toBeVisible();
    await navegador.fill('computadoras');
    await page.keyboard.press('Enter');
    await page.pause();

    await expect(page).toHaveTitle(/computadoras/i);
    await page.pause();

    await page.locator("span[class='ui-search-filter-name']:has-text('PC de Escritorio')").click();
    await page.pause();

    const categorias = page.locator("span[itemprop='name']:has-text('PC de Escritorio')");
    await expect(categorias).toBeVisible();
    await page.pause();
  });
});

test.describe('Pruebas de ordenamiento', () => {
  
  test('Ordenar por menor precio', async ({ page }) => {
    await page.goto('https://listado.mercadolibre.com.mx/computadoras#D[A:computadoras]/');
    await page.pause();

    const abrir = page.locator("span[class='andes-dropdown__display-values']:has-text('Más relevantes')");
    await abrir.click();
    await page.pause();

    const abrir2 = page.locator("span[class='andes-list__item-primary']:has-text('Menor precio')");
    await abrir2.click();
    await page.pause();
  });

  test('Ordenar por precio mayor', async ({ page }) => {
    await page.goto('https://listado.mercadolibre.com.mx/computadoras#D[A:computadoras]/');
    await page.pause();

    const abrir = page.locator("span.andes-dropdown__display-values:has-text('Más relevantes')");
    await abrir.click();
    await page.pause();

    const abrir2 = page.locator("span[class='andes-list__item-primary']:has-text('Mayor precio')");
    await abrir2.click();
    await page.pause();
  });

  test('Ordenar varias veces', async ({ page }) => {
    await page.goto('https://listado.mercadolibre.com.mx/computadoras#D[A:computadoras]/');
    await page.pause();

    const abrir = page.locator("span.andes-dropdown__display-values:has-text('Más relevantes')");
    await abrir.click();
    await page.pause();

    const select = page.locator("span[class='andes-list__item-primary']:has-text('Menor precio')");
    await select.click();
    await page.pause();

    const abrir2 = page.locator("span.andes-dropdown__display-values:has-text('Menor precio')");
    await abrir2.click();
    await page.pause();

    const select2 = page.locator("span[class='andes-list__item-primary']:has-text('Mayor precio')");
    await select2.click();
    await page.pause();

    const abrir3 = page.locator("span.andes-dropdown__display-values:has-text('Mayor precio')");
    await abrir3.click();
    await page.pause();

    const select3 = page.locator("span[class='andes-list__item-primary']:has-text('Más relevantes')");
    await select3.click();
    await page.pause();
  });
});

test.describe('Pruebas de categorias', () => {
  test("Software", async ({ page }) => {
    await page.goto('https://listado.mercadolibre.com.mx/computadoras#D[A:computadoras]/');
    await page.pause();

    const abrir = page.locator("a[href='https://listado.mercadolibre.com.mx/computadoras_FiltersAvailableSidebar?filter=category']:has-text('Mostrar más')");
    await expect(abrir).toBeVisible();
    await abrir.click();
    await page.pause();

    const select = page.locator("span[class='ui-search-search-modal-filter-name']:has-text('Software')");
    await expect(select).toBeVisible();
    await select.click();
    await page.pause();

    const categorias = page.locator("span[itemprop='name']:has-text('Software')");
    await expect(categorias).toBeVisible();
    await page.pause();
  });

  test("Mejores vendedores", async ({ page }) => {
    await page.goto('https://listado.mercadolibre.com.mx/computadoras#D[A:computadoras]/');
    await page.pause();

    const select = page.locator("span[class='ui-search-filter-name']:has-text('Mejores vendedores')");
    await expect(select).toBeVisible();
    await select.click();
    await page.pause();

    const categorias = page.locator("div[class='andes-tag__label']:has-text('Mejores vendedores')");
    await expect(categorias).toBeVisible();
    await page.pause();
  });
  test("Envio gratis", async ({ page }) => {
    await page.goto('https://listado.mercadolibre.com.mx/computadoras#D[A:computadoras]/');
    await page.pause();

    const click = page.locator("label[for='shipping_cost_highlighted_free']:has-text('Envío gratis')");
    await expect(click).toBeVisible();
    await click.click();
    await page.pause();

    await expect(page).toHaveURL(/computadoras_CostoEnvio_Gratis_/i);
    await page.pause();
  });
});

test.describe("Pruebas de paginas de producto", () => {
  test("Boton carrito", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const boton = page.locator('button[id=":R9j9o5l9im:"]');
    await expect(boton).toBeVisible();
    await page.pause();
  });

  test("Imagenes", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const imagen1 = page.locator("img[srcset='https://http2.mlstatic.com/D_NQ_NP_2X_658862-CBT77085701694_062024-F.webp 2x']");
    await expect(imagen1).toBeVisible();
    await page.pause();

    const imagen2 = page.locator("img[srcset='https://http2.mlstatic.com/D_Q_NP_2X_658862-CBT77085701694_062024-R.webp 2x']");
    await expect(imagen2).toBeVisible();
    await page.pause();

    const imagen3 = page.locator("img[srcset='https://http2.mlstatic.com/D_Q_NP_2X_731563-CBT80357060637_102024-R.webp 2x']");
    await expect(imagen3).toBeVisible();
    await page.pause();

    const imagen4 = page.locator("img[srcset='https://http2.mlstatic.com/D_Q_NP_2X_725191-CBT80101303998_102024-R.webp 2x']");
    await expect(imagen4).toBeVisible();
    await page.pause();

    const imagen5 = page.locator("img[srcset='https://http2.mlstatic.com/D_Q_NP_2X_962203-CBT80101303996_102024-R.webp 2x']");
    await expect(imagen5).toBeVisible();
    await page.pause();

  });

  test("Descripciones", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const caracteristicas = page.locator("section[class='ui-vpp-highlighted-specs pl-45 pr-45']");
    await expect(caracteristicas).toBeVisible();
    await page.pause();

    const descripcion = page.locator("div[class='ui-pdp-description']");
    await expect(descripcion).toBeVisible();
    await page.pause();
  }); 

  test("Calificaciones", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const calif = page.locator("a[class='ui-pdp-review__label ui-pdp-review__label--link']");
    await expect(calif).toBeVisible();
    await page.pause();
  }); 

  test("Precio producto", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const precio = page.locator("div[class='ui-pdp-price__second-line']");
    await expect(precio).toBeVisible();
    await page.pause();
  }); 

  test("Comprar ahora", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const comprar = page.locator("span[class='andes-button__content']:has-text('Comprar ahora')");
    await expect(comprar).toBeVisible();
    await page.pause();
  }); 

  test("Favoritos", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const favoritos = page.locator("svg[class='ui-pdp-icon ui-pdp-icon--bookmark ui-pdp-bookmark__icon-bookmark']");
    await expect(favoritos).toBeVisible();
    await page.pause();
  }); 

  test("Preguntas y respuestas", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const costo = page.locator("a[class='ui-pdp-action-modal__link andes-button andes-button--quiet andes-button--medium ui-pdp-questions__link']:has-text('Costo y tiempo de envío')");
    await expect(costo).toBeVisible();
    await costo.click();
    await page.pause();

    const cerrar1 = page.locator("path[d='M4.35156 5.19496L9.15406 9.99746L4.35156 14.8L5.20009 15.6485L10.0026 10.846L14.7963 15.6397L15.6449 14.7912L10.8511 9.99746L15.6449 5.20371L14.7963 4.35518L10.0026 9.14894L5.20009 4.34644L4.35156 5.19496Z']");
    await expect(cerrar1).toBeVisible();
    await cerrar1.click();
    await page.pause();

    const devolucion = page.locator("a[class='ui-pdp-action-modal__link andes-button andes-button--quiet andes-button--medium ui-pdp-questions__link']:has-text('Devoluciones gratis')");
    await expect(devolucion).toBeVisible();
    await devolucion.click();
    await page.pause();

    const cerrar2 = page.locator("path[d='M4.35156 5.19496L9.15406 9.99746L4.35156 14.8L5.20009 15.6485L10.0026 10.846L14.7963 15.6397L15.6449 14.7912L10.8511 9.99746L15.6449 5.20371L14.7963 4.35518L10.0026 9.14894L5.20009 4.34644L4.35156 5.19496Z']");
    await expect(cerrar2).toBeVisible();
    await cerrar2.click();
    await page.pause();

    const pago = page.locator("a[class='ui-pdp-action-modal__link andes-button andes-button--quiet andes-button--medium ui-pdp-questions__link']:has-text('Medios de pago y promociones')");
    await expect(pago).toBeVisible();
    await pago.click();
    await page.pause();

    const cerrar3 = page.locator("path[d='M4.35156 5.19496L9.15406 9.99746L4.35156 14.8L5.20009 15.6485L10.0026 10.846L14.7963 15.6397L15.6449 14.7912L10.8511 9.99746L15.6449 5.20371L14.7963 4.35518L10.0026 9.14894L5.20009 4.34644L4.35156 5.19496Z']");
    await expect(cerrar3).toBeVisible();
    await cerrar3.click();
    await page.pause();

    const garantia = page.locator("a[class='ui-pdp-action-modal__link andes-button andes-button--quiet andes-button--medium ui-pdp-questions__link']:has-text('Garantía')");
    await expect(garantia).toBeVisible();
    await garantia.click();
    await page.pause();

    const cerrar4 = page.locator("path[d='M4.35156 5.19496L9.15406 9.99746L4.35156 14.8L5.20009 15.6485L10.0026 10.846L14.7963 15.6397L15.6449 14.7912L10.8511 9.99746L15.6449 5.20371L14.7963 4.35518L10.0026 9.14894L5.20009 4.34644L4.35156 5.19496Z']");
    await expect(cerrar4).toBeVisible();
    await cerrar4.click();
    await page.pause();
  }); 
});

test.describe("Pruebas de carrito", () =>{
  test("Agregar al carrito", async ({page}) =>{
    await page.goto('https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM#polycard_client=search-nordic&position=52&search_layout=stack&type=item&tracking_id=8009cbe5-f005-4177-8924-88504231a6ad/');
    await page.pause();

    const agregar = page.locator("button[id=':R9j9o5l9im:']:has-text('Agregar al carrito')");
    await expect(agregar).toBeVisible();
    await agregar.click();
    await page.pause();

    const carrito = page.locator("a[id='nav-cart']");
    await expect(carrito).toBeVisible();
    await carrito.click();

    const verificar = page.locator("a[href='https://articulo.mercadolibre.com.mx/MLM-1516305584-ordenador-portatil-hp-14-intel-n4120-64-emmc-4-gb-hd-win-_JM?variation=175416349955']:has-text('Ordenador Portátil Hp 14 Intel N4120 (64 Emmc + 4 Gb) Hd Win')");
    await expect(verificar).toBeVisible();
    await page.pause();
  }); 
});
test('Cargar Página', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  await page.pause();
})

test('Logotipo Visible', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  await expect(page.locator("a[class='nav-logo']:has-text('Mercado Libre México - Donde comprar y vender de todo')")).toBeVisible();
  await page.pause();
})

test('Menú Categorías', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  await expect(page.locator("a[class='nav-menu-categories-link']:has-text('Categorías')")).toBeVisible();
  await page.pause();
})

test('Más Vendidos', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  await expect(page.locator("h1[class='header-title-hidden']:has-text('Mas vendidos en Mercado Libre Mexico')")).toBeVisible();
  await page.pause();
})

test('Inicio Sesión', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  await expect(page.locator("a[data-link-id='login']:has-text('Ingresa')")).toBeVisible();
  await page.pause();
})

test('Botón Búsqueda', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  const searchInput = page.locator("input[id='cb1-edit']");
  await expect(searchInput).toBeVisible();
  await searchInput.fill("xbox");
  await page.keyboard.press('Enter');
  await page.locator("button[class='nav-search-btn']").click();
  const element = page.locator('span[class="ui-search-search-result__quantity-results"]');
  await expect(element).toBeVisible();
  const titleText = await element.textContent();
  expect(titleText?.toLowerCase()).toContain('resultados');
  await page.pause();
})

test('Enter Búsqueda', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  const searchInput = page.locator("input[id='cb1-edit']");
  await expect(searchInput).toBeVisible();
  await searchInput.fill("xbox");
  await page.keyboard.press('Enter');
  const element = page.locator('span[class="ui-search-search-result__quantity-results"]');
  await expect(element).toBeVisible();
  const titleText = await element.textContent();
  expect(titleText?.toLowerCase()).toContain('resultados');
  await page.pause();
})

test('Navegar Categoría', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  await page.locator("a[class='nav-menu-categories-link']:has-text('Categorías')").click();
  //await page.locator("a:has-text('Vehículos')").waitFor({ state: 'visible' });
  await page.locator("a[href='https://www.mercadolibre.com.mx/vehiculos/#menu=categories']:has-text('Vehículos')").click();
  await expect(page).toHaveTitle(/Autos, Camionetas, Motos y más | Mercado Libre /);
  await page.pause();
})

test('Carrito Visible', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  await expect(page.locator("i[class='nav-icon-cart']")).toBeVisible();
  await page.pause();
})

test('Título Búsqueda', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  const searchInput = page.locator("input[id='cb1-edit']");
  await expect(searchInput).toBeVisible();
  await searchInput.fill("xbox");
  await page.keyboard.press('Enter');
  await expect(page).toHaveTitle(/Xbox en Black Friday | MercadoLibre 📦/);
  await page.pause();
})

test('Búsqueda Relevante', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  const searchInput = page.locator("input[id='cb1-edit']");
  await expect(searchInput).toBeVisible();
  await searchInput.fill("xbox");
  await page.keyboard.press('Enter');
  const element = page.locator('a[href*="MLM40176492"]:has-text("Consola Xbox Series S Edición Digital")');
  await expect(element).toBeVisible();
  const titleText = await element.textContent();
  expect(titleText?.toLowerCase()).toContain('xbox');
  await page.pause();
})

test('Búsqueda Mayúsculas', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  const searchInput = page.locator("input[id='cb1-edit']");
  await expect(searchInput).toBeVisible();
  await searchInput.fill("XBOX");
  await page.keyboard.press('Enter');
  const element = page.locator('a[href*="MLM16650345"]:has-text("Consola Xbox Series S All Digital 512gb Color Blanco")');
  await expect(element).toBeVisible();
  const titleText = await element.textContent();
  expect(titleText?.toLowerCase()).toContain('xbox');
  await page.pause();
})

test('Caracteres Especiales', async({page}) => {
  await page.goto('https://www.mercadolibre.com.mx/');
  const searchInput = page.locator("input[id='cb1-edit']");
  await expect(searchInput).toBeVisible();
  await searchInput.fill("Televisión 4k!");
  await page.keyboard.press('Enter');
  const element = page.locator('a[href*="MLM36338363"]:has-text("Pantalla 50\\" Tcl 4k Hdr Google Tv 50s451g Negro")');
  await expect(element).toBeVisible();
  const titleText = await element.textContent();
  expect(titleText?.toLowerCase()).toContain('tv');
  expect(titleText?.toLowerCase()).toContain('4k');
  await page.pause();
})
test.describe('Registro', () => {

  test('Registro valido', async ({ page }) => {

    // Navegar a la página de inicio de sesión de Mercado Libre
    await page.goto('https://www.mercadolibre.com.mx');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Blackfriday en Mercado Libre Mexico/);
    await page.pause();


    // Esperar que el botón "Crea tu cuenta" sea visible y hacer clic en él
    const crearCuentaButton = page.locator('a[href="https://www.mercadolibre.com.mx/registration?confirmation_url=https%3A%2F%2Fwww.mercadolibre.com.mx%2F#nav-header"]');
    await crearCuentaButton.click();  // Hacer clic en "Crea tu cuenta"
    await page.pause();

    // Comprobar que la URL ha cambiado a la página de registro (asegurándonos de que contiene una cadena como "register")
    await expect(page).toHaveURL(/registration/);  // Verifica que la URL contiene "registration"
    await page.pause();

    const AgregarEmailButton = page.locator('text=Agregar');
    await AgregarEmailButton.click();
    await page.pause();

    // Verificar que el cuadro de texto de email está presente
    const emailInput = page.locator('input[type="email"]'); // Selector para el cuadro de texto del email
    await expect(emailInput).toBeVisible();
    await page.pause();

    // Ingresar un email válido y verificar
    await emailInput.fill('villagomezmichelle02@gmail.com');
    const emailValue = await emailInput.inputValue();
    expect(emailValue).toBe('villagomezmichelle02@gmail.com'); // Verifica que se haya ingresado el email
    await page.pause();

    const terminos = page.locator('input[id="policies"]');
    await terminos.check();  // Check en Terminos y condiciones
    await page.pause();

    const continuar = page.locator('span[class="andes-button__content"]');
    await continuar.click();  // Click continuar
    await page.pause();

    const botonElegirNombre = page.locator('span[class="andes-button__text"]');
    await botonElegirNombre.click();
    await page.pause();

    const nombreInput = page.locator('input[id="firstName"]'); // Selector para el cuadro de texto del nombre
    await expect(nombreInput).toBeVisible();
    await page.pause();

    await nombreInput.fill('Michlpruebassi');
    const nombreValue = await nombreInput.inputValue();
    expect(nombreValue).toBe('Michlpruebassi'); // Verifica que se haya ingresado el nombre
    await page.pause();

    const ApellidoInput = page.locator('input[id="lastName"]'); // Selector para el cuadro de texto del nombre
    await expect(ApellidoInput).toBeVisible();
    await page.pause();

    await ApellidoInput.fill('LopezPruebass');
    const ApellidoValue = await ApellidoInput.inputValue();
    expect(ApellidoValue).toBe('LopezPruebass'); // Verifica que se haya ingresado el nombre
    await page.pause();

    const continuar2 = page.locator('span[class="andes-button__text"]');
    await continuar2.click();  // Click continuar
    await page.pause();

    const botonValidar = page.locator('span[class="andes-button__text"]');
    await botonValidar.click();
    await page.pause();

    const celInput = page.locator('input[id=":R1ot1:"]'); // Selector para el cuadro de texto del numero de celular
    await expect(celInput).toBeVisible();
    await page.pause();

    await celInput.fill('4498070910');
    const celValue = await celInput.inputValue();
    expect(celValue).toBe('4498070910'); // Verifica que se haya ingresado el numero
    await page.pause();

    const check2 = page.locator('input[id="contact-checkbox"]'); // Check de sms
    await expect(check2).toBeVisible();
    await page.pause();

    const botonCrearContraseña = page.locator('span[class="andes-button__content"]');
    await botonCrearContraseña.click();
    await page.pause();

    const conInput = page.locator('input[id="enter-password"]'); // Selector para el cuadro de texto de contraseña
    await expect(conInput).toBeVisible();
    await page.pause();

    await conInput.fill('Pruebasunitarias02!');
    const conValue = await conInput.inputValue();
    expect(conValue).toBe('Pruebasunitarias02!'); // Verifica que se haya ingresado el numero
    await page.pause();

    const con2Input = page.locator('input[id="confirm-password"]'); // Selector para el cuadro de texto de contraseña
    await expect(con2Input).toBeVisible();
    await page.pause();

    await con2Input.fill('Pruebasunitarias02!');
    const con2Value = await con2Input.inputValue();
    expect(con2Value).toBe('Pruebasunitarias02!'); // Verifica que se haya ingresado el numero
    await page.pause();

    const botonContinuar3 = page.locator('span[class="andes-button__content"]');
    await botonContinuar3.click();
    await page.pause();

    await expect(page).toHaveTitle(/Blackfriday en Mercado Libre Mexico/);
    await page.pause();

  });


  test('Registro invalido', async ({ page }) => {

    // Navegar a la página de inicio de sesión de Mercado Libre
    await page.goto('https://www.mercadolibre.com.mx');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Blackfriday en Mercado Libre Mexico/);
    await page.pause();


    // Esperar que el botón "Crea tu cuenta" sea visible y hacer clic en él
    const crearCuentaButton = page.locator('a[href="https://www.mercadolibre.com.mx/registration?confirmation_url=https%3A%2F%2Fwww.mercadolibre.com.mx%2F#nav-header"]');
    await crearCuentaButton.click();  // Hacer clic en "Crea tu cuenta"
    await page.pause();

    // Comprobar que la URL ha cambiado a la página de registro (asegurándonos de que contiene una cadena como "register")
    await expect(page).toHaveURL(/registration/);  // Verifica que la URL contiene "register"
    await page.pause();

    const AgregarEmailButton = page.locator('text=Agregar');
    await AgregarEmailButton.click();
    await page.pause();

    // Verificar que el cuadro de texto de email está presente
    const emailInput = page.locator('input[type="email"]'); // Selector para el cuadro de texto del email
    await expect(emailInput).toBeVisible();
    await page.pause();

    await emailInput.fill('usuario_invalido');
    const invalidEmailValue = await emailInput.inputValue();
    expect(invalidEmailValue).toBe('usuario_invalido'); // Verifica el ingreso del email inválido
    await page.pause();

    // Hacer clic en un botón de "Enviar" y validar errores
    const submitButton = page.locator('button[type="submit"]'); // Cambia por el selector de tu botón
    await submitButton.click();
    await page.pause();

    // Validar que aparece un mensaje de error para el email inválido
    const errorMessage = page.locator('span[id="enter-email-input-message"]');
    await expect(errorMessage).toBeVisible();
    await expect(errorMessage).toHaveText(/Usa el formato nombre@ejemplo.com./i); // Verifica el texto del error
    await page.pause();

  });

});


test.describe('Sesion', () => {

  test('Inicio cierre sesion', async ({ page }) => {

    await page.goto('https://www.mercadolibre.com.mx');
    // Verificar el título de la página
    //await expect(page).toHaveTitle(/Mercado Libre México - Envíos Gratis en el día/);
    await page.pause();

    const botonLog = page.locator('a[data-link-id="login"]');
    await botonLog.click();
    await page.pause();

    const emailInput2 = page.locator('input[type="email"]'); // Selector para el cuadro de texto del email
    await expect(emailInput2).toBeVisible();
    await page.pause();

    // Ingresar un email válido y verificar
    await emailInput2.fill('michellelopez020202@gmail.com');
    const emailValue2 = await emailInput2.inputValue();
    expect(emailValue2).toBe('michellelopez020202@gmail.com'); // Verifica que se haya ingresado el email
    await page.pause();

    const botonContinuar = page.locator('button[type="submit"]');
    await botonContinuar.click();
    await page.pause();

    const botonContinuar2 = page.locator('button[type="submit"]');
    await botonContinuar2.click();
    await page.pause();

    const botonSMS = page.locator('button[class="andes-list__item-action"]', { hasText: 'SMS' });
    await botonSMS.click();
    await page.pause();

    await expect(page).toHaveTitle(/Blackfriday en Mercado Libre Mexico/);
    await page.pause();

    const botonPerfil = page.locator('span[class="nav-header-username"]');
    await botonPerfil.hover(); // Simula el pasar del mouse
    await page.waitForTimeout(1000);

    const botonSalir = page.locator('a[href="https://www.mercadolibre.com/jms/mlm/lgz/logout?go=https://www.mercadolibre.com.mx#menu-user"]'); // Usa un selector más específico si es necesario
    await botonSalir.click();
    await page.pause();


  });

  test('Inicio cierre sesion 2', async ({ page }) => {

    await page.goto('https://www.mercadolibre.com.mx');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Blackfriday en Mercado Libre Mexico/);
    await page.pause();

    const botonLog = page.locator('a[data-link-id="login"]');
    await botonLog.click();
    await page.pause();

    const emailInput2 = page.locator('input[type="email"]'); // Selector para el cuadro de texto del email
    await expect(emailInput2).toBeVisible();
    await page.pause();

    // Ingresar un email válido y verificar
    await emailInput2.fill('michellelopez020202@gmail.com');
    const emailValue2 = await emailInput2.inputValue();
    expect(emailValue2).toBe('michellelopez020202@gmail.com'); // Verifica que se haya ingresado el email
    await page.pause();

    const botonContinuar = page.locator('button[type="submit"]');
    await botonContinuar.click();
    await page.pause();

    const contraseñainput = page.locator('input[type="password"]'); // Selector para el cuadro de texto de la contraseña
    await expect(contraseñainput).toBeVisible();
    await page.pause();

    // Ingresar la contraseña
    await contraseñainput.fill('Pruebasunitarias02!');
    const contraseñavalue = await contraseñainput.inputValue();
    expect(contraseñavalue).toBe('Pruebasunitarias02!'); // Verifica que se haya ingresado la contraseña
    await page.pause();

    const botonContinuar2 = page.locator('button[type="submit"]', { hasText: 'Iniciar Sesión' });
    await botonContinuar2.click();
    await page.pause();


    await expect(page).toHaveTitle(/Blackfriday en Mercado Libre Mexico/);
    await page.pause();

    const botonPerfil = page.locator('span[class="nav-header-username"]');
    await botonPerfil.hover(); // Simula el pasar del mouse
    await page.waitForTimeout(1000);

    const botonSalir = page.locator('a[href="https://www.mercadolibre.com/jms/mlm/lgz/logout?go=https://www.mercadolibre.com.mx#menu-user"]'); // Usa un selector más específico si es necesario
    await botonSalir.click();
    await page.pause();

    await expect(page).toHaveTitle(/Blackfriday en Mercado Libre Mexico/);
    await page.pause();

  });

});


test.describe('Pagos', () => {

  test('Comprar', async ({ page }) => {

    await page.goto('https://www.mercadolibre.com.mx');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Blackfriday en Mercado Libre Mexico/);
    await page.pause();

    const botonLog = page.locator('a[data-link-id="login"]');
    await botonLog.click();
    await page.pause();

    const emailInput2 = page.locator('input[type="email"]'); // Selector para el cuadro de texto del email
    await expect(emailInput2).toBeVisible();
    await page.pause();

    // Ingresar un email válido y verificar
    await emailInput2.fill('michellelopez020202@gmail.com');
    const emailValue2 = await emailInput2.inputValue();
    expect(emailValue2).toBe('michellelopez020202@gmail.com'); // Verifica que se haya ingresado el email
    await page.pause();

    const botonContinuar = page.locator('button[type="submit"]');
    await botonContinuar.click();
    await page.pause();

    const contraseñainput = page.locator('input[type="password"]'); // Selector para el cuadro de texto de la contraseña
    await expect(contraseñainput).toBeVisible();
    await page.pause();

    // Ingresar la contraseña
    await contraseñainput.fill('Pruebasunitarias02!');
    const contraseñavalue = await contraseñainput.inputValue();
    expect(contraseñavalue).toBe('Pruebasunitarias02!'); // Verifica que se haya ingresado la contraseña
    await page.pause();

    const botonContinuar2 = page.locator('button[type="submit"]', { hasText: 'Iniciar Sesión' });
    await botonContinuar2.click();
    await page.pause();



    const searcInput = page.locator("input[id='cb1-edit']");
    await expect(searcInput).toBeVisible();
    await page.pause();

    await searcInput.fill("vestido");
    await page.keyboard.press('Enter');
    await page.pause();


    await expect(page).toHaveTitle(/Vestido | MercadoLibre 📦/);

    const vestido = page.locator("h2.poly-box.poly-component__title", { hasText: "Vestido De Fiesta Con Diseño De Princesa Sirena Para Niñas" });
    await expect(vestido).toBeVisible(); // Verifica que sea visible
    await vestido.click(); // Haz clic en el elemento


    await page.pause();
    await expect(page).toHaveTitle(/Vestido Largo Casual Sexy Maria Bela Modelo Baku | Envío gratis/);

    const talla = page.locator('a[title="100"]'); // Cambia el índice según corresponda
    await talla.click();
    await page.pause();

    const comprar = page.locator('button[class="andes-button andes-spinner__icon-base ui-pdp-action--primary andes-button--loud"]');
    await expect(comprar).toBeVisible();
    await comprar.click();
    await page.pause();

    const dir = page.locator('p[data-id="card_description"]');
    await expect(dir).toBeVisible();
    await page.pause();

    const contin = page.locator('button[id=":R3a9i:"]');
    await expect(contin).toBeVisible();
    await contin.click();
    await page.pause();

    const contin2 = page.locator('button[id=":R3r9i:"]');
    await expect(contin2).toBeVisible();
    await contin2.click();
    await page.pause();

    await expect(page).toHaveURL(/checkout/);
    await page.pause();


  });

  

});

test.describe('Filtros', () => {

  test('Precio', async ({ page }) => {

    await page.goto('https://www.mercadolibre.com.mx');
    // Verificar el título de la página
    //await expect(page).toHaveTitle(/Mercado Libre México - Envíos Gratis en el día/);
    await page.pause();

    const searcInput = page.locator("input[id='cb1-edit']");
    await expect(searcInput).toBeVisible();
    await page.pause();

    await searcInput.fill("vestido");
    await page.keyboard.press('Enter');
    await page.pause();
    await expect(page).toHaveTitle(/Vestido | MercadoLibre 📦/);
    await page.pause();

    const precio1 = page.locator('input[data-testid="Minimum-price"]');
    await precio1.click();
    await page.pause();

    await precio1.fill("200");
    await page.pause();

    const precio2 = page.locator('input[data-testid="Maximum-price"]');
    await precio2.click();
    await page.pause();

    await precio2.fill("500");
    await page.pause();

    await page.keyboard.press('Enter');
    await page.pause();

    await expect(page).toHaveURL(/vestido_PriceRange_200-500/);
    await page.pause();

  });

  test('Marca', async ({ page }) => {

    await page.goto('https://listado.mercadolibre.com.mx/vestido#D[A:vestido,L:undefined]');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Vestido | MercadoLibre 📦/);
    await page.pause();

    const tienda = page.locator('span.ui-search-filter-name:has-text("Solo tiendas oficiales")');
    await tienda.click();
    await page.pause();

    await expect(page).toHaveURL(/vestido_Tienda_all/);

    const marca = page.locator('span.ui-search-filter-name:has-text("C&A")');
    await marca.click();
    await page.pause();

    await expect(page).toHaveURL(/3DMarca%26applied_filter_order/);
    const marca2 = page.locator('div.andes-tag__label', { hasText: 'C&A' });
    await expect(marca2).toBeVisible();
    await page.pause();
  });

  test('Variosfiltros', async ({ page }) => {

    await page.goto('https://listado.mercadolibre.com.mx/vestido#D[A:vestido,L:undefined]');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Vestido | MercadoLibre 📦/);
    await page.pause();

    const filtro1 = page.locator('span.ui-search-filter-name:has-text("Mujer")');
    await filtro1.click();
    await page.pause();

    const filtro2 = page.locator('span.ui-search-filter-name:has-text("2XG")');
    await filtro2.click();
    await page.pause();

    const filtro3 = page.locator('span.ui-search-filter-name:has-text("Desde 25% OFF")');
    await filtro3.click();
    await page.pause();

    const productos = page.locator('div[class="ui-search-main ui-search-main--only-products ui-search-main--with-topkeywords"]');
    await expect(productos).toBeVisible();
    await page.pause();
  });

  test('Condicion', async ({ page }) => {

    await page.goto('https://listado.mercadolibre.com.mx/celulares#D[A:celulares]');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Celulares en Black Friday | MercadoLibre 📦/);
    await page.pause();

    const condicion = page.locator('h3.ui-search-filter-dt-title:has-text("Condición")');
    await expect(condicion).toBeVisible();
    await page.pause();

    const filtro = page.locator('span.ui-search-filter-name:has-text("Usado")');
    await filtro.click();
    await page.pause();

    const productos = page.locator('div[class="ui-search-main ui-search-main--only-products ui-search-main--with-topkeywords"]');
    await expect(productos).toBeVisible();
    await page.pause();

    await expect(page).toHaveURL(/usado/);
    await page.pause();

  });

  test('Ubicacion', async ({ page }) => {

    await page.goto('https://listado.mercadolibre.com.mx/celulares#D[A:celulares]');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Celulares en Black Friday | MercadoLibre 📦/);
    await page.pause();

    const ubicacion = page.locator('h3.ui-search-filter-dt-title:has-text("Ubicación")');
    await expect(ubicacion).toBeVisible();
    await page.pause();

    const filtro = page.locator('span.ui-search-filter-name:has-text("Estado De México")');
    await filtro.click();
    await page.pause();

    const productos = page.locator('div[class="ui-search-main ui-search-main--only-products ui-search-main--with-topkeywords"]');
    await expect(productos).toBeVisible();
    await page.pause();

    await expect(page).toHaveURL(/celulares-smartphones-en-estado-de-mexico/);
    await page.pause();
  });

  test('Enviogratis', async ({ page }) => {

    await page.goto('https://listado.mercadolibre.com.mx/celulares#D[A:celulares]');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Celulares en Black Friday | MercadoLibre 📦/);
    await page.pause();

    const envio = page.locator('h3.ui-search-filter-dt-title:has-text("Costo de envío")');
    await expect(envio).toBeVisible();
    await page.pause();

    const filtro = page.locator('span.ui-search-filter-name:has-text("Envío gratis")');
    await filtro.click();
    await page.pause();

    const productos = page.locator('div[class="ui-search-main ui-search-main--only-products ui-search-main--with-topkeywords"]');
    await expect(productos).toBeVisible();
    await page.pause();

    await expect(page).toHaveURL(/celulares_CostoEnvio_Gratis/);
    await page.pause();

  });

  test('Categoria', async ({ page }) => {

    await page.goto('https://www.mercadolibre.com.mx');
    // Verificar el título de la página
    //await expect(page).toHaveTitle(/Mercado Libre México - Envíos Gratis en el día/);
    await page.pause();

    const botoncategoria = page.locator('a[data-js="nav-menu-categories-trigger"]');
    await botoncategoria.hover(); // Simula el pasar del mouse
    await page.waitForTimeout(1000);

    const categoria = page.locator('a[href="https://www.mercadolibre.com.mx/c/juegos-y-juguetes#menu=categories"]'); // Usa un selector más específico si es necesario
    await categoria.click();
    await page.pause();

    await expect(page).toHaveURL(/juegos-y-juguetes#menu=categories/);
    await page.pause();

  });

  test('Desactivar', async ({ page }) => {

    await page.goto('https://listado.mercadolibre.com.mx/vestido#D[A:vestido,L:undefined]');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Vestido | MercadoLibre 📦/);
    await page.pause();

    const filtro = page.locator('span.ui-search-filter-name:has-text("Mujer")');
    await filtro.click();
    await page.pause();

    await expect(page).toHaveURL(/mujer/);
    await page.pause();

    const filtroquitar = page.locator('div.andes-tag__label:has-text("Mujer")');
    await filtroquitar.click();
    await page.pause();

    await expect(page).toHaveURL(/unapplied_filter/);
    await page.pause();

  });

  test('masrelevantes', async ({ page }) => {

    await page.goto('https://listado.mercadolibre.com.mx/vestido#D[A:vestido,L:undefined]');
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Vestido | MercadoLibre 📦/);
    await page.pause();

    const masrelevantes = page.locator('span.andes-dropdown__display-values:has-text("Más relevantes")');
    await masrelevantes.click();
    await page.pause();

    const menorprecio = page.locator('span.andes-list__item-primary:has-text("Menor precio")');
    await menorprecio.click();
    await page.pause();

    const vestidos = page.locator('div[class="ui-search-main ui-search-main--only-products ui-search-main--with-topkeywords"]');
    await expect(vestidos).toBeVisible();
    await page.pause();

  });

});
