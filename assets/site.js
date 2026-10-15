(function(){
  var root=document.documentElement, btns=document.querySelectorAll('.lang button');
  function set(l){
    root.setAttribute('data-lang',l); root.setAttribute('lang',l);
    var t=root.getAttribute('data-title-'+l); if(t){document.title=t;}
    btns.forEach(function(b){b.setAttribute('aria-pressed', b.dataset.set===l?'true':'false');});
    try{localStorage.setItem('vcg-lang',l);}catch(e){}
  }
  var saved=null; try{saved=localStorage.getItem('vcg-lang')||localStorage.getItem('rv-lang');}catch(e){}
  var q=null; try{q=new URLSearchParams(location.search).get('lang');}catch(e){}
  var init=q||saved||((navigator.language||'es').toLowerCase().indexOf('en')===0?'en':'es');
  set(init==='en'?'en':'es');
  btns.forEach(function(b){b.addEventListener('click',function(){set(b.dataset.set);});});

  var burger=document.querySelector('.burger'), menu=document.querySelector('.menu');
  if(burger&&menu){burger.addEventListener('click',function(){
    var open=menu.classList.toggle('open'); burger.setAttribute('aria-expanded',open?'true':'false');
  });}

  document.querySelectorAll('.yr').forEach(function(e){e.textContent=new Date().getFullYear();});
  document.querySelectorAll('.js-mail').forEach(function(a){a.href='mailto:'+a.dataset.u+'@'+a.dataset.d;});
  document.querySelectorAll('.js-wa').forEach(function(a){a.href='https://wa.me/'+a.dataset.n;});
})();
