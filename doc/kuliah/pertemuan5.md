Latar Belakang:
Membuat Shapefile
Mengedit Shapefile?
Menghapus Shapefile?
<br>
Kali ini saya akan sedikit memberikan tutorial bagaimana cara membuat data geospasial. pada pembuatan data geospasial ini saya menggunakan library pyshp.
Berikut cara membuat data geospasial :
Masuk Python<br>
Import Shapefile<br>
sf = shapefile.writer(shpetype=1)<br>
sf.point(10.10)<br>
sf.field('warung','D','40')<br>
sf.field('pemilik','D','80')<br>
sf.record('cuangki','Sakedik nikmat')<br>
sf.save('datacuangki.shp')<br>

Selanjutnya Mengedit Data Geospasial. Berikut cara mengedit data geospasial :<br>
1. Masuk Python <br>
2. Ganti sf = shapefile.writer(shpetype=1) dengan sf = shapefile.editor(datacuangki.shp)<br>
3. Langkah berikutnya sama dengan langkah pembuatan data geospasial<br>

cara menghapus/delete data geospasial:
<br>
1. sf.delete(10)<br>
2. sf.shapes()[10].points[(10,10])<br>
3. sf.points[10,10]<br>
4. sf.record('warteg')<br>
5. sf.save('datawarteg.shp')<br>

Penutup:<br>
Kesimpulan
<br>
dari pembuatan blogini kali ini kita dapat mengetahui cara membuat, mengubah dan menghapus data geospasial.

Saran:
<br>
Agar lebih mudahnya untuk mengetahui cara nya alangkah baiknya untuk mempraktikannya sendiri.<br>

