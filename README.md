# argparse-to-boutiques
GitHub Action to create a [Boutiques descriptor](https://boutiques.github.io/) for a Python CLI based on `argparse.ArgumentParser`

The workflow is two steps:

1. `main.py` imports a tool's argparse parser and dumps it to a JSON
   descriptor (via [`argdump`](https://github.com/styx-api), styx's
   superset of the Boutiques format).
2. The [styx](https://github.com/styx-api/styx) CLI compiles that JSON into
   a plain Boutiques descriptor with `--backend boutiques`.

`main.py` takes the parser's module location, the name of the
parser-builder, and an output path. The styx step is run through `npx`, so
nothing needs to be installed beyond Node.js.

## Examples with BIDS-apps

### MRIQC

```bash
python main.py mriqc.cli.parser _build_parser --output mriqc.json
npx -y --package @styx-api/cli styx build mriqc.json --out styx-out_mriqc --backend boutiques
```

### rsHRF

```bash
python main.py rsHRF.CLI get_parser --output rsHRF.json
npx -y --package @styx-api/cli styx build rsHRF.json --out styx-out_rsHRF --backend boutiques
```

In each case the tool's package must be importable (e.g. installed into the
active environment) so that `main.py` can import its parser module.
