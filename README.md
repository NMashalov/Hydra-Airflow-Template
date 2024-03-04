# Hydra Airflow Templater

![](/assets/arch.excalidraw.png)

Cli app for templating [Airflow](https://airflow.apache.org/) `dag.py` through [Hydra](https://hydra.cc/) and with [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) for python. Rather technical solution, but might be useful as starting point for developing etl tool.

Key features are:
- support of multiple environments 🧰 and ability to share settings with use of hydra [default](https://hydra.cc/docs/tutorials/basic/your_first_app/defaults/)
- arbitrary template 🧾 with help of keywords
- ability to give default using hydra [configstore](https://hydra.cc/docs/tutorials/structured_config/config_store/)
- python api and cli support

### Configuration structure 🏠

For templating structure should be like


![](/assets/structure.excalidraw.png)

See settings example in test [folder](/test/) for ocr pipeline:
```
.
├── ocr
│   ├── action
│   │   ├── extract.yaml
│   │   ├── load.yaml
│   │   └── transform.yaml
│   ├── dag
│   │   └── base.yaml
│   ├── default.yaml
│   └── dev.yaml
└── tmp.txt
```

For flexible configuring ui check my other project [PyVisGraph](https://github.com/NMashalov/PyVisGraph)

### Installation 

```
pip install hydra_airflow_templater
```


### Quick start

Templation is done by command line



- `env` - is used in case of environment  


### FAQ


Q: How to "use hydra cli" in Python

A: Hydra [docs](https://hydra.cc/docs/1.0/experimental/compose_api/#internaldocs-banner) have Compose api for this purpose:
```python
cfg = compose(config_name="config", overrides=["db=mysql", "db.user=me"])
```
I use it 

Q:
A: If you want Hydra to save the overridden configuration to a file, use the --cfg or -c option followed by the path where you want to save the configuration.

### Contact

Open issue on github or contact me on mashalov.ne@gmail.com
