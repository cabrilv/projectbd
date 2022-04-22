{
 "cells": [
  {
   "cell_type": "code",
   #"execution_count": null,
   "id": "c25d21ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "__author__ = \"Natalia Lopez - Fernanda Zambrano - Cristian Abril\"\n",
    "__maintainer__ = \"Consulta Condiciones de Ruta generando información relevante acerca de accidentalidad de acuerdo con un historial de accidentes\"\n",
    "__copyright__ = \"Copyright 2022 - Asignatura Big Data\"\n",
    "__version__ = \"0.0.1\"\n",
    "\n",
    "try:\n",
    "    import pandas as pd\n",
    "    import json\n",
    "    import requests\n",
    "    import re\n",
    "    import datetime\n",
    "    import imageio\n",
    "    import matplotlib.pyplot as plt\n",
    "    from bs4 import BeautifulSoup\n",
    " \n",
    " \n",
    "    \n",
    "except Exception as exc:\n",
    "    print('Module(s) {} are missing.:'.format(str(exc)))\n",
    "    \n",
    "#API_Key = \"GSJGa9GXlivtdLdhN4c6bLtBxORp3r7i\"\n",
    "API_Key =\"i9GmAvGupLXiOhmONgrpi1GzbaDvlyUg\"\n",
    "    \n",
    "class tomtom(object):\n",
    "    \n",
    "    \n",
    "    def __init__(self, inicio=None, fin=None):\n",
    "        self.data = None\n",
    "        self.inicio=inicio\n",
    "        self.fin=fin\n",
    "        \n",
    "    \n",
    "    \n",
    "    def consulta_georeferenciacion(self):\n",
    "        lugares = [self.inicio,self.fin]\n",
    "        latitud =[]\n",
    "        longitud=[]\n",
    "        for lugar in lugares:\n",
    "            url = \"https://api.tomtom.com/search/2/search/\"+lugar+\".json?countrySet=CO&language=es-419&minFuzzyLevel=1&maxFuzzyLevel=2&view=Unified&relatedPois=off&entityTypeSet=Municipality&key=\"\n",
    "            #url = \"https://api.tomtom.com/search/2/search/\"+lugar+\".json?limit=1&countrySet=CO%2FCOL&language=es-419&extendedPostalCodesFor=Geo&minFuzzyLevel=1&maxFuzzyLevel=2&idxSet=Geo&view=Unified&mapcodes=Local&relatedPois=off&entityTypeSet=Municipality&key=\"\n",
    "            r = requests.get(url+API_Key)\n",
    "            c = r.json()\n",
    "            latitud.append(c['results'][0]['position']['lat'])\n",
    "            longitud.append(c['results'][0]['position']['lon'])\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
