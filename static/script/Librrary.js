var library = [
    '../static/Wallpaper Library/22fdaf7b49d3921b32fed46f05fc70d.png',
    '../static/Wallpaper Library/90b75d737f8e20de83691de5ae777e5.png',
    '../static/Wallpaper Library/3838e67b48882cd053774562228bf37.png',
    '../static/Wallpaper Library/8903a69045826893020d60b5ff0f3a1.png',
    '../static/Wallpaper Library/39253fc4b3800481e96c1f44173209b.png',
    '../static/Wallpaper Library/961233bf8be67f0051d7975270a80f0.jpg',
    '../static/Wallpaper Library/a8bc126c9f4d28f4b7fc53655f5416e.png',
    '../static/Wallpaper Library/e5d019c1d26cf8e3addc8b35390f88f.png',
    '../static/Wallpaper Library/e0503b1bcde4228d906a6196b5a8d37.png',
    '../static/Wallpaper Library/fe7d3ad0f52e294d7a05ca3d966b9f2.png',
]
var imgs =document.getElementById('imgs')
var n=0
for(var i=0;i<library.length;i++){
    var imgbox=document.getElementsByClassName('imgbox')
    imgs.innerHTML+=`<img src="${library[i]}">`
}
// for(var j=1;j<10;j++){
//     imgs.innerHTML+=`<img>`
// }