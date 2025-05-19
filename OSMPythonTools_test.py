import marimo

__generated_with = "0.13.10"
app = marimo.App(width="medium")


@app.cell
def _():
    from OSMPythonTools.api import Api
    api = Api()
    way = api.query('way/5887599')
    return (way,)


@app.cell
def _(way):
    way.tag("website")
    return


@app.cell
def _():
    return


@app.cell
def _():
    from OSMPythonTools.overpass import Overpass
    overpass = Overpass()
    result = overpass.query('way["name"="Stephansdom"]; out body;')
    return (result,)


@app.cell
def _(result):
    stephansdom = result.elements()[0]
    return (stephansdom,)


@app.cell
def _(stephansdom):
    stephansdom.tag('name:en')
    # "Saint Stephen's Cathedral"
    '%s %s, %s %s' % (stephansdom.tag('addr:street'), stephansdom.tag('addr:housenumber'), stephansdom.tag('addr:postcode'), stephansdom.tag('addr:city'))
    # 'Stephansplatz 3, 1010 Wien'
    stephansdom.tag('building')
    # 'cathedral'
    stephansdom.tag('denomination')
    # 'catholic'
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
