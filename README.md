# Ransomware Payload - Agent Plugin for Infection Monkey

## Introduction

Ransomware Payload is an Agent Plugin for
[Infection Monkey](https://www.akamai.com/infectionmonkey) that
can simulate a ransomware attack by encrypting files on the target machine.
It uses a simple bit-flipping algorithm to encrypt files, and the encryption
is reversible by simply running the plugin again.

For more information, see the [Ransomware Payload Plugin
documentation](https://techdocs.akamai.com/infection-monkey/docs/ransomware-simulation).

For our Ransomware tutorial see [Ransomware
Tutorial](https://techdocs.akamai.com/infection-monkey/docs/ransomware).

## Development
### Setting up the development environment

To create the resulting Ransomware archive, follow these steps:

1. **Clone the Repository**

    ```sh
    $ git clone https://github.com/guardicode/ransomware-payload.git
    $ cd ransomware-payload
    ```

1. **Install development dependencies**

    This project uses [Poetry](https://python-poetry.org/) for managing
    dependencies and virtual environments, and
    [pre-commit](https://pre-commit.com/) for managing pre-commit hooks.

    ```sh
    $ pip install pre-commit poetry
    $ pre-commit install -t pre-commit
    $ poetry install
    ```

### Running the test suite

The test suite can be run with the following command:

```sh
poetry run pytest
```

### Building the plugin

To build the plugin, run the [Agent Plugin
Builder](https://github.com/guardicode/agent-plugin-builder/).

```sh
poetry run build_agent_plugin .
```

The build tool will create `Ransomware-payload.tar`, which can be [installed in
the Monkey Island](https://techdocs.akamai.com/infection-monkey/docs/plugins).
