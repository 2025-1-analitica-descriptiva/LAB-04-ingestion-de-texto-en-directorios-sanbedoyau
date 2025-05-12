# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa

from homework.utils import load_file, create_ouptput_directory
from random import shuffle
import pandas as pd

def pregunta_01():
    '''
    La información requerida para este laboratio esta almacenada en el
    archivo 'files/input.zip' ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta 'input' en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados 'train_dataset.csv' y 'test_dataset.csv'. Estos
    archivos deben estar ubicados en la carpeta 'output' ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * target: Sentimiento de la frase. Puede ser 'positive', 'negative'
        o 'neutral'. Este corresponde al nombre del directorio donde se
        encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    '''
    emotions = ['positive', 'negative', 'neutral']
    in_path = 'files/input'
    out_path = 'files/output'
    test = []
    train = []
    for emotion in emotions:
        test += load_file(f'{in_path}/test/{emotion}')
        train += load_file(f'{in_path}/train/{emotion}')
    shuffle(test)
    shuffle(train)
    test_data = {'phrase': [phrase for _, phrase in test],
                 'target': [emotion for emotion, _ in test]}
    train_data = {'phrase': [phrase for _, phrase in train],
                  'target': [emotion for emotion, _ in train]}
    test_dataset = pd.DataFrame(test_data)
    train_dataset = pd.DataFrame(train_data)
    create_ouptput_directory(out_path)
    test_dataset.to_csv(f'{out_path}/test_dataset.csv')
    train_dataset.to_csv(f'{out_path}/train_dataset.csv')