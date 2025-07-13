# Assessing Peruvian Poverty from Satellite Imagery

## Requirements

### Data

#### Peruvian Household Survey (ENAHO)

Follow these steps to download the housing and household characteristics of a specific year:

1. Go to ["Sistema de Microdatos"][inei-microdatos] of the Peruvian Institute of Statistics and Informatics (INEI).

2. Navigate to the "Consulta por Encuestas" tab.

3. From the "ENCUESTA" dropdown, select "ENAHO Metodología ACTUALIZADA".

4. From the next dropdown, select "Condiciones de Vida y Pobreza - ENAHO".

5. Choose your target year from the "AÑO" dropdown.

6. From the "Período" dropdown, select "Anual - (Ene-Dic)".

7. Look for the first row in the results table and click "SPSS" under the "Descarga" column.

8. Save the downloaded ZIP file in the `data/raw` directory of this repository.

### Dependencies

> *This project uses a [`conda`][conda] environment to manage the dependencies.*

Run the following command to create an environment with the required dependencies:

```sh
conda env create --file environment.yml
```

[inei-microdatos]: https://proyectos.inei.gob.pe/microdatos/
[conda]: https://docs.conda.io
