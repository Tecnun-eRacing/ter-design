# Todo

## General
- [ ] Dibujo general de que cosas hay dnd y que hacen
- [x] Lista de la compra inicial y comprarla
- [x] Comprobar esta misma lista y añadir lo que falte
- [ ] Documentar cosas a nivel general (Wire harness y esas movidas q terminan siendo utiles, no hace falta explicar cada placa a detalle)
- [x] Encontrar un Conformal Coating bueno
- [x] ¿Posiblemente migrar esto a la intranet de miguel?, me sigue gustando mas tener asi para tener un control de versiones decente
- [ ] Ser ESOs

## ACCU

### Cosas estructurales
- [x] Diseño en CAD
- [ ] Ver como enfriar
- [ ] Elegir ubicacion placas
- [ ] Manufacturar
- [ ] Revision Carrito
  - [ ] Cambiar ruedas/frenos
  - [ ] Mirar para hacer q todo quede mas clean (si vamos sobrados de tiempo)

### HV
- [ ] Fusibles
  - [ ] El gordo
  - [ ] Los pequeños
- [ ] Cableado de alta
  - [ ] El gordo
  - [ ] Trifasico guapo
- [ ] AIRs
- [ ] Parametros y curvas de las celdas para el SOC

### LV
- [ ] Diseño del Slave
  - [x] Ver como conectarlo a las busbar y a el accu
  - [x] Ver si el valor de la R del npn tiene que ser mas pequeña 
  - [x] Botones temps y volts
  - [ ] Placa de testing de Slave
  - [ ] Slave Testeado
  - [ ] Carrier del Slave
- [ ] AMS
  - [ ] SOC
- [ ] IMD 300k
- [ ] Voltage Indicator
- [ ] Precarga
- [ ] Sensor de corriente
- [ ] DCDC

## TS Enclosures

### Inverters + PDB + Discharge + TSMP + TSAL RED
- [ ] Diseño (Que todo encaje)
- [ ] PDB
- [ ] Placa Descarga + TSMP + TSAL RED
- [ ] Decirle cosas a los inverters (Configurarlo y ver como se le manda torque)
- [ ] Sensor de corriente del BSPD (Sino en la caja del datalogger si queda mejor ahi)
  - [ ] Revisar potencialmente pillar uno nuevo con menos deriva termica o que su placa tenga correccion

### Datalogger
- [ ] Diseño caja datalogger

### HVD
- [ ] Ver dnd ponerlo y ponerlo

### Cableado
- [ ] Ver como llevar a los motores de alante, firewall y toda la movida

## LV

### Pantalla
- [ ] Hacer pantalla basica con leds (master)
- [ ] Hacer pantalla guapa en volante (slave)

### RJs
- [x] Propuesta de cambiar los RJs
- [x] Decidir si cambiarlos o no
- [ ] Cambiarlo todas las placas
- [ ] Spliters nuevos

### EBS
- [ ] Arreglar el pin de reset
- [ ] Fusible de RES truco (No le da la corriente ni de cerca)

### PEDAL
- [ ] Pedal de freno con region de regen
- [ ] Potencialmente que lea presion de ambas lineas de freno pq ahora una la lee la pedal y la otra el EBS
- [ ] Cambiar amplis de pedal por los tlv9001 sot 23-2 pin compatible (o unos buenos)

### Refri
- [ ] Huellas ampli lm321
- [ ] Revision general pq ya no tiene un xt60

### Control
(en realidad esto es un poco sugerencia pq hare el codigo de la ecu y luego ya vere como cuadra esto)
- [ ] Regen suave
- [ ] Torque vectoring
- [ ] Refri con PID
- [ ] Cosas guapas con la PI

### Llaves
- [ ] Repasar que tiene que ir alimentado de que llave
- [ ] TSMPs, LVGnd, 24v, USB, RJ, Setas...
- [ ] Repaso del SDC
  - [ ] ¿Motores externos?

### Sensores random
- [ ] Pedir que sensores random quiere la gente

[LEER ZONA DE ORGANIZACION DE AQUI](./ideas.md)
