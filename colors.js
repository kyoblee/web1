var Links = {
  setColor: function(color) {
//    var alist = document.querySelectorAll('a');
//    var i = 0;
//    while (i < alist.length) {
//      alist[i].style.color = color;
//      i += 1;
//    }
    $('a').css('color', color) // JQuery
  }
}

var Body = {
  setColor: function(color) {
    // document.querySelector('body').style.color = color;
    // 위 라인을 JQuery로 대체
    $('body').css('color', color);
  },
  setBackgroundColor: function(color) {
    // document.querySelector('body').style.backgroundColor = color;
    // 위 라인을 JQuery로 대체 
    $('body').css('backgroundColor', color)
  }
}

function nightDayHandler(self) {
  var target = document.querySelector('body');
  if (self.value === 'night') {
    Body.setBackgroundColor('black');
    Body.setColor('white');
    self.value = 'day';
    Links.setColor('powderblue');
  } else {
    Body.setBackgroundColor('white');
    Body.setColor('black');
    self.value = 'night';
    Links.setColor('blue');
  }
}