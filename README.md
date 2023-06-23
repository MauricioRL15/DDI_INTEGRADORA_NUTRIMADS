# DDI_INTEGRADORA_NUTRIMADS

## Documento de Requerimientos de software *NUTRIMADS*
### 02/05/2023


|    ![Imagen 1](https://github.com/DaniArroyo104/NUTRIMADS_utileria/blob/main/logo_empresa.png?raw=true)    |    ![Imagen 2](https://github.com/DaniArroyo104/NUTRIMADS_utileria/blob/main/logo_app.png?raw=true)    |
| :----------------------------------: | :----------------------------------: |
|          NUTRIMADS logo Empresa         |          NUTRIMADS logo App         |
  

#### Versión 1.0.0

### Organigrama de equipo
<p align="center">
  <img src="https://github.com/DaniArroyo104/NUTRIMADS_utileria/blob/main/organigramaNew.jpg?raw=true" alt="Organigrama de equipo">
</p>

### Historial de versiones

| Fecha      | Versión  |  Autor| Organización | Descripción |
|------------|----------|---------------|--------------|-------------|
| 11/06/2023 | 1.0      | Daniel Arroyo Méndez  |   NUTRIMADS       |Primer versión de NUTRIMADS|

## Informacion del proyecto

### Aprobaciones

| Nombre y Apellido      | Cargo  |  Departamento u Organización | Fecha | Firma |
|------------|----------|---------------|--------------|-------------|
| Arely Aguilar Farias | DB Manager      | NUTRIMADS | 02/05/23 | |
| Sandra Aguilar Santos | Líder / Desarrollador Frontend      | NUTRIMADS | 02/05/23 | |
| Daniel Arroyo Méndez | Documentador     | NUTRIMADS | 02/05/23 | |
| Mauricio Ramírez López | Desarrollador Backend     | NUTRIMADS | 02/05/23 | |

### Propósito

NUTRI MADS 1.0.0
Este documento cubre en su mayoría la totalidad documentada del software en proceso.
Se definen roles de usuarios, alcance, funcionalidades del mismo, requerimientos funcionales y no funcionales, además de características de usuarios que serán incluidos en el sistema de software.

### Alcance del producto
Aplicación para Wear OS con la función de brindar información nutricional de los alimentos consumidos a lo largo del día, proporcionar información valiosa sobre su ingesta de nutrientes y ayudarles a tomar decisiones más saludables en cuanto a su alimentación.
- Ayudar a los usuarios a tomar decisiones más saludables.
- Crear conciencia alimentaria.
- Realizar un seguimiento de su ingesta diaria

### Funcionalidades

Estas funcionalidades pueden ayudar a los usuarios a tener un mayor control y comprensión de su ingesta nutricional diaria, fomentando hábitos alimentarios más saludables y apoyando su bienestar general.

**1. Búsqueda de alimentos:** Proporcionar una función de búsqueda que permita a los usuarios encontrar alimentos específicos y obtener detalles nutricionales sobre ellos.

**2. Base de datos de alimentos:** Contar con una amplia base de datos de alimentos que incluya información nutricional completa y actualizada sobre una amplia variedad de alimentos.

**3. Seguimiento de alimentos:** Permitir a los usuarios registrar y hacer un seguimiento de los alimentos que consumen a lo largo del día, ya sea a través de la búsqueda, selección de alimentos de una lista predefinida.

**4. Información nutricional:** Proporcionar información nutricional básica para cada alimento.

**5. Recomendaciones de alimentos:** Ofrecer recomendaciones de alimentos saludables y equilibrados en función de las metas nutricionales establecidas por el usuario.

**6. Historial y análisis:** Mantener un historial de los alimentos consumidos y permitir a los usuarios revisar su ingesta nutricional a lo largo del tiempo. También podría proporcionar gráficos y análisis para ayudar a los usuarios a comprender sus patrones de alimentación y realizar ajustes si es necesario.

### Requerimientos Funcionales
1- Registro manual de alimentos: Permitir al usuario registrar manualmente los alimentos que consume a lo largo del día, ingresando los alimentos y las porciones consumidas.

2- Base de datos de alimentos: Contar con una base de datos completa de alimentos que incluya información nutricional  básica. Los usuarios podrán seleccionar los alimentos de esta base de datos al registrar su consumo.

3- Cálculo de ingesta nutricional: Realizar un seguimiento de la ingesta diaria de nutrientes y calcular automáticamente la cantidad consumida de calorías, proteínas, carbohidratos, grasas y otros nutrientes relevantes a partir de los alimentos registrados manualmente.

4- Recomendaciones personalizadas: Proporcionar recomendaciones personalizadas sobre la ingesta diaria en función de los objetivos de salud y las características individuales del usuario.

5- Alertas y recordatorios: Emitir alertas y recordatorios para ayudar al usuario a mantener un seguimiento regular de su ingesta de alimentos a lo largo del día.


### Requerimientos No Funcionales

1- Usabilidad y experiencia de usuario: La aplicación debe ser intuitiva, fácil de usar y adaptada a la pantalla y capacidades de un dispositivo wearable como Wear OS. La interfaz debe ser legible y eficiente para facilitar la interacción del usuario.

2- Rendimiento y tiempo de respuesta: La aplicación debe ser ágil y responder de manera rápida a las interacciones del usuario, evitando demoras significativas en la carga de datos o en los cálculos nutricionales.

3- Disponibilidad y compatibilidad: La aplicación debe estar disponible y funcionar de manera confiable en dispositivos Wear OS y ser compatible con diferentes versiones del sistema operativo.

4- Compatibilidad: Asegurar que la aplicación sea compatible con diferentes versiones del sistema operativo Wear OS y se adapte correctamente a las características del dispositivo wearable.

### Reglas de Negocio

- Registro de alimentos obligatorio: El usuario debe registrar al menos una comida al día para poder acceder a las funcionalidades de la aplicación.

- Sugerencias de alimentos saludables: La aplicación proporcionará sugerencias de alimentos saludables basados en las preferencias y necesidades del usuario, pero no se responsabiliza de la exactitud o idoneidad de dichas sugerencias.

- Notificaciones: La aplicación enviará una notificación recordando al usuario que registre sus comidas y brindando consejos o recordatorios relacionados con la alimentación saludable, pero no será responsable si el usuario no recibe o no actúa según estas notificaciones.

- Responsabilidad del usuario: El usuario es responsable de verificar la exactitud de la información ingresada sobre los alimentos consumidos, así como de consultar a un profesional de la salud antes de realizar cambios significativos en su alimentación.

- Información educativa: La aplicación proporcionará información nutricional y consejos relacionados con la alimentación saludable, pero no reemplaza el asesoramiento médico profesional. Se recomienda que los usuarios consulten a un profesional de la salud para obtener recomendaciones personalizadas.

- Compatibilidad de dispositivos: La aplicación solo estará disponible para dispositivos Wear OS que cumplan con los requisitos de hardware y software especificados.