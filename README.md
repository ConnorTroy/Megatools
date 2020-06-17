# Megatools (1.10.3)

(UNDER CONSTRUCTION)

Simple python Megatools wrapper



[![Codacy Badge](https://app.codacy.com/project/badge/Grade/726d6cfd795242b587cdb8b8e9308f7c)](https://www.codacy.com/manual/Harkame/Megatools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Harkame/Megatools&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/20a4bd84eaac4d6cdc9a/maintainability)](https://codeclimate.com/github/Harkame/Megatools/maintainability)

[Megatools](https://megatools.megous.com)
[Megatools (github)](https://github.com/megous/megatools)

## Installation

``` shell

pip install megatools

```

## Usage

### Initialization

``` python

from megatools import Megatools

megatools = Megatools() #Use megatools command in path

#OR

megatools = Megatools(executable="D:\\megatools\\megatools.exe")

```

### Get mega link filename

``` python

megatools.get_file_name("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

```

### dl - download exported files from mega.nz

``` python
# Basic usage

megatools.dl("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY")

# With all optional arguments and their default values

megatools.dl("https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY",
  path=None,
  no_progress=False,
  print_names=False,
  disable_resume=False,
  username=None,
  password=None,
  reload=False,
  limit_speed=0,
  proxy=None,
  netif=None,
  ip_proto=None,
  config=None,
  ignore_config_file=False,
  display_output=False,
  debug=None,
  version=None)
```

### Another commands incomming
