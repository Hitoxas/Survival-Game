//Inventory functionality

let inventoryVisible = false;

function updateInventory() {
    fetch('/inventory')
        .then(response => response.json())
        .then(data => {
            let output = "<h3>Your Inventory:</h3><ul>";
            for (const [item, amount] of Object.entries(data)) {
                output += `<li>${item}: ${amount}</li>`;
            }
            output += "</ul>";
            const inventoryDiv = document.getElementById('inventory');
            inventoryDiv.innerHTML = output;
        });
}

function toggleInventory() {
    const inventoryDiv = document.getElementById('inventory');
    inventoryVisible = !inventoryVisible;

    if (inventoryVisible) {
        inventoryDiv.style.display = 'block';
        updateInventory();
    } else {
        inventoryDiv.style.display = 'none';
    }
}

//Crafting Menu functionality

function updateCraftingMenu() {
    const craftingDiv = document.getElementById('crafting');

    fetch('/crafting')
        .then(res => res.json())
        .then(data => {
            let html = '<h3>Crafting Menu:</h3><ul>';
            data.forEach(item => {
                const costText = Object.entries(item.cost)
                    .map(([key, val]) => `${key}: ${val}`)
                    .join(', ');

                const disabled = item.available ? '' : 'disabled';

                html += `<li>
                    <button onclick="craftItem('${item.id}')" ${disabled}>${item.name}</button>
                    <span> (${costText})</span>
                </li>`;
            });
            html += '</ul>';
            craftingDiv.innerHTML = html;
        });
}

function craftItem(endpoint) {
    fetch(`/${endpoint}`, {
        method: 'POST'
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('output').innerText = data.message;
        if (inventoryVisible) updateInventory();
        if (craftingVisible) updateCraftingMenu();
    });
}

let craftingVisible = false;

function toggleCrafting() {
    const craftingDiv = document.getElementById('crafting');
    craftingVisible = !craftingVisible

    if (craftingVisible) {
        craftingDiv.style.display = 'block';
        updateCraftingMenu();

    } else {
        craftingDiv.style.display = 'none';
    }
}


// Recource Collection functions

function collectFiber() {
    fetch('/collect_fiber', {
            method:'POST'
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerText = data.message;
            if (inventoryVisible) updateInventory();
            if (craftingVisible) updateCraftingMenu();
        });
}
function collectStick() {
    fetch('/collect_stick', {
            method:'POST'
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerText = data.message;
            if (inventoryVisible) updateInventory();
            if (craftingVisible) updateCraftingMenu();
        });
}
 function collectStone() {
    fetch('/collect_stone', {
            method:'POST'
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerText = data.message;
            if (inventoryVisible) updateInventory();
            if (craftingVisible) updateCraftingMenu();
        });
}

// Crafting specific item functions

function craftRope() {
    fetch('/craft_rope', {
            method:'POST'
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerText = data.message;
            if (inventoryVisible) updateInventory();
            if (craftingVisible) updateCraftingMenu();
        });
}

function craftWoodenHandle() {
    fetch('/craft_wooden_handle', {
            method:'POST'
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerText = data.message;
            if (inventoryVisible) updateInventory();
            if (craftingVisible) updateCraftingMenu();
        });
}