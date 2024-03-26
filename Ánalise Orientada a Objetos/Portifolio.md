+-----------------------------------+
| Veículo |
+-----------------------------------+
| - númeroPlaca: String |
| - cor: String |
| - ano: Integer |
| - tipoCombustível: String |
| - númeroPortas: Integer |
| - quilometragem: Double |
| - renavam: String |
| - chassi: String |
| - valorLocação: Double |
+-----------------------------------+
| + getDetalhesVeículo(): String |
+-----------------------------------+
| 1
|
v _
+-----------------------------------+
| Modelo |
+-----------------------------------+
| - nomeModelo: String |
+-----------------------------------+
| + getDetalhesModelo(): String |
+-----------------------------------+
| 1
|
v _
+-----------------------------------+
| Marca |
+-----------------------------------+
| - nomeMarca: String |
+-----------------------------------+
| + getDetalhesMarca(): String |
+-----------------------------------+

+-----------------------------------+
| Cliente |
+-----------------------------------+
| - nome: String |
| - cpf: String |
| - endereço: String |
| - telefone: String |
+-----------------------------------+
| + alugarVeículo(veículo: Veículo) |
| + devolverVeículo(veículo: Veículo)|
+-----------------------------------+
| _
|
v _
+-----------------------------------+
| Locação |
+-----------------------------------+
| - dataHoraLocação: DateTime |
| - dataHoraDevolução: DateTime |
+-----------------------------------+
| + getDetalhesLocação(): String |
+-----------------------------------+
