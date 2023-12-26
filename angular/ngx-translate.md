# Múltiples Idiomas con ngx-translate
- `npm install @ngx-translate/core --save`
- `npm install @ngx-translate/http-loader --save`
- or `npm install @ngx-translate/core @ngx-translate/http-loader --save`
- Configurar `ngx-translate` en `app.mudule.ts` o en un módulo específico para la internacionalización.

```TypeScript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { TranslateModule, TranslateLoader } from '@ngx-translate/core';
import { TranslateHttpLoader } from '@ngx-translate/http-loader';

export function createTranslateLoader(http: HttpClient) {
  return new TranslateHttpLoader(http, './assets/i18n/', '.json');
}

@NgModule({
  declarations: [
    // tus componentes aquí
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: createTranslateLoader,
        deps: [HttpClient]
      }
    })
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```
- Crear archivos JSON para cada idioma en la carpeta `assets/i18n/`.
- assets/i18n/en.json:
```json
{
  "welcome": "Bienvenido a mi sitio web!",
  "aboutMe": "Sobre mí",
  "featuredProject": "Proyecto destacado"
  // más traducciones...
}
```
- assets/i18n/es.json: 
```json
{
  "welcome": "Bienvenido a mi sitio web!",
  "aboutMe": "Sobre mí",
  "featuredProject": "Proyecto destacado"
  // más traducciones...
}
```

## Recursos Adicionales
- [ngx-bootstrap](https://valor-software.com/ngx-bootstrap/#/documentation)
- [Creating an Angular Portfolio Website](https://www.youtube.com/playlist?list=PLN0Th-4WgKrUVQlqa14mUDeymTW1luznW)
- [Portfolio Template](https://github.com/StyvenSoft/portfolio-template)
- [App con múltiples idiomas usando ngx-translate con Angular / Ionic](https://www.youtube.com/watch?v=bVIH8f0Oyv0)