function get_shops_from_regions() {
    clean_shop_list();
    var node;
    for (var i = 0; i < regions.length; i++) {
        node = document.getElementById('region_' + regions[i].id);
        for (var j = 0; j < node.children.length; j++) {
            if (node.children[j].nodeName == 'svg') {
                node = node.children[j];
                if (node.hasChildNodes()) {
                    for (var k = 0; k < shops.length; k++) {
                        if (shops[k].region_id == regions[i].id) {
                            add_shop_to_list(k);
                        }
                    }
                }
            }
        }
    }
    control_shuffle_display();
}

function add_shop_to_list(index) {
    var node = document.getElementById('shop_list');
    var li = document.createElement('li');
    li.setAttribute('id', 'shop_' + index);
    li.innerHTML = shops[index].name;
    node.appendChild(li);
}

function clean_shop_list() {
    var node = document.getElementById('shop_list');
    while (node.firstChild) {
        node.removeChild(node.firstChild);
    }
}

function shops_shuffle() {
    var shop_list = document.getElementById('shop_list').children;
    var number = Math.floor(Math.random() * shop_list.length);
    var node = document.getElementById('shuffle_result');
    node.innerHTML = shop_list[number].innerHTML;
}

function control_shuffle_display() {
    var node = document.getElementById('btn_shuffle');
    if (document.getElementById('shop_list').hasChildNodes()) {
        node.style.display = 'inline';
    }
    else {
        node.style.display = 'none';
    }
}