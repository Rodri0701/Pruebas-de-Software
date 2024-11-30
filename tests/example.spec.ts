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