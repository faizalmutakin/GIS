Latar Belakang Masalah<br>
implementasi GIS benyak untuk dilakukan .Tetapi untuk itu kita harus
belajar terlebih dahulu cara manipulasi data (retrieve , update delete).
kali ini saya akan menjelaskan data shapefile geospasial dengan CRUD.
Cara Create shapefile <br>
Cara Update shapefile <br>
cara Delete shapefile <br>


CREATE DATA<br>
langkah-langkahnya adalah sebagai berikut:
1.cara-import shapefile<br>
2.cara-instansiasi writer method<br>
  caranya adalah:<br>
	Sf = shapefile.Writer(param)<br>
	param adlah memilih shapetype:<br>
	type 1<br>
	type 3<br>
	type 5<br>
3.melakukan method dbf dan shp<br>

shapefile (shp)
Menambahkan record (ESRI)
sf.point (x,y)<br>
sf.line = (parts: [[x,y],[z,w],...])<br>
sf.poly = (parts: [[x,y],[z,w],...])<br>

Databasefile (dbf)<br>
Langkah yang perlu dilakukan yaitu :<br>
1.Buatlah atribut terlebih dahulu dan tambahkan record.<br>
	Contoh:<br>
	sf.field (‘Nama Field’, ’D’, ’40’)<br>
Dari keterangng  diatas C itu adalah Character atau tipe datanya, dan 40 adalah length atau panjang data nya.
Pada contoh di atas dapat diartikan bahwa nama field dengan panjang 40 karakter.<br>
2. Menambahkan record  seperti contoh di bawah ini<br>
	sf.record(‘Bandung’)<br>
	sf.record(‘Bandung’,’Lembang’)<br>
3.Setelah itu simpan seperti di bawah ini:<br>
	sf.save(‘namefile.shp’)<br>
UPDATE ATAU EDIT<br>
disini ada langkah-langkah untuk melakukan editing.<br>
Import shape file<br>
1.Sf = shape file.editor(rumahmakan.shp)<br>
2.Sf.point(17,12,0,0)<br>
3.Sf.record (‘nikmat’)<br>
4.Sf.save<br>
5.Sf.save (‘rumahmakan.shp’)<br>
6.a=shapefile.reoder(‘rumahmakan.shp’)<br>
7.a.recorders()<br>
8.a.shapes().points<br>
9.a.shape()[0]<br>
10.a.shape()[0] points<br>

[(10,0,10,0)]

DELETE<br>
Sf.delete(0)<br>
a.shapes()[0].points [(10,0,10,0)]<br>
sf.points [17,12,0,0]<br>
sf.record(‘nikmat’)<br>
sf.saver(‘rmmkn.shp’)<br>

Penutup<br>
Kesimpulan<br>
Dari kesimpulan kali ini sya menimpulkan bahwa dapat mengetahui cara
melakukan (Create, Update, Delete).

Saran<br>
untuk lebih jelasnya alangkah baiknya untuk melakukan mempraktikan secara
langsung,dan memperbanyak latihan.
