# Librería Date Holidays

## Instalar
`npm install date-holidays`

## Configurar

### Uso
```ts
    import Holidays from 'date-holidays';

    private holidays = new Holidays('CO');
```

### Función para días festivos
```ts
    isHoliday(date: Date): boolean {
    return !!this.holidays.isHoliday(date);
    }
```

### Filtro
```ts
    dateFilter = (date: Date | null): boolean => {
    if (!date) return false;
    const day = date.getDay();
    const isHoliday = this.isHoliday(date);
    return !isHoliday;
    };
```

## Carga Lazy

### Crea un archivo de declaración (Opcional)
`src/types/date-holidays.d.ts`
```ts
    declare module 'date-holidays';
```

### Configurar
```ts
  private holidays: any = null;

  async loadHolidays() {
    if (!this.holidays) {
      const Holidays = (await import('date-holidays')).default;
      this.holidays = new Holidays('CO');
    }
  }

  isHoliday(date: Date): boolean {
    return !!this.holidays?.isHoliday(date);
  }
```

### Agregar ChangeDetectorRef
```ts
    import { ChangeDetectionStrategy, Component, inject, ChangeDetectorRef } from '@angular/core';

    private cdr = inject(ChangeDetectorRef);

    async loadHolidays() {
    if (!this.holidays) {
        const Holidays = (await import('date-holidays')).default;
        this.holidays = new Holidays('CO');
        this.cdr.markForCheck(); // refresca el datepicker
    }
    }

    dateFilter = (date: Date | null): boolean => {
    if (!date) return false;
    const day = date.getDay();
    const isHoliday = this.isHoliday(date);
    return !isHoliday;
    };
```