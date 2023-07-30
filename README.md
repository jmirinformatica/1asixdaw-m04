#FpInfor #Daw #DawMp4 #Asix #AsixMp4

# 1asixdaw-m04-xslt

## Setup

### Python Virtual Environment

Crea l'entorn:

    python3 -m venv .venv

Activa'l:

    source .venv/bin/activate

Instal·la el requisits:

    pip install -r requirements.txt

Alternativament, els requisits es poden instal·lar manualment:

    pip install -U pip
    pip install -U flask python-dotenv lxml requests

Per a generar el fitxer de requiriments:

    pip freeze > requirements.txt

Per desactivar l'entorn:

    deactivate

### Fitxer .env

Crea el fitxer `.env` a partir del `.env.exemple`

### Inicia l'aplicació

Executa:

    flask run

I obre un navegador a l'adreça: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### DEBUG

Des de l'opció de `Run and Debug`, crea un fitxer animenat `launch.json` amb el contingut següent:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "MY APP",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "wsgi.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```