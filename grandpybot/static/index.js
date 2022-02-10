let text_Area = document.getElementById("question");

const click_Button = document.getElementById('button');

click_Button.addEventListener("click", function(event){
    event.preventDefault();
    if (text_Area.value !== ""){
        fetch("/search?question="+text_Area.value)
            .then(function (response){
                    if (response.status !== 200) {
                        console.log('Erreur: ' + response.status);
                    return;
                    };
                    response.json().then(display) 
            });

    function display(data) {
        var d = new Date();
        var getMinutes = d.getMinutes();
        if (getMinutes.toString().length === 1) {
            minutes = '0' + getMinutes;
        }else{
            minutes = getMinutes;
        };
        var hours = d.getHours() + ":" + minutes;
        var d = new Date();
        var hours = d.getHours() + ":" + d.getMinutes()
        let elt_to_publish = 
            `<div class="row justify-content-end">
                <p class="col-8 border rounded border-dark">${text_Area.value}<br/><span class="time-left">${hours}</span></p>
                <img id="users" class="col-2 align-self-end" src="../static/img/users.png" alt="Grandpybot-image">
                
            </div>
            <div class="row">
                <img id="papymg" class="col-2" src="../static/img/papy_head.png" alt="Grandpybot-image">
                <p class="col-8 border rounded border-dark">
                    ${data.pos_story}<br><br> Si tu veux en savoir plus, va voir sur 
                    <a target="_blank" href="https://fr.wikipedia.org/wiki/${data.user_input}">Wikipedia</a><br/>
                    <span class="time-left">${hours}</span>
                </p>
            </div>`;
        document.getElementById('description').innerHTML = document.getElementById('description').innerHTML + elt_to_publish;
        initMap(data)
        scroller = document.getElementById('toScroll')
        scroller.scrollTop = scroller.scrollHeight;
        return data;
    };

    let map;
    function initMap(data) {
        const mapper = document.getElementById("mapSpace");
        const mapContain = document.createElement("map")
        let space = `<p id='searchTitle' class="row justify-content-center mb-0">${data.clean_input.toUpperCase()}</p><div id="map" class="container" style="height: 300px;"></div>`;
        mapper.innerHTML = space;
        mapper.appendChild(mapContain);
        const myLatLng = { lat: data.infos.lati, lng: data.infos.lngi };
        map = new google.maps.Map(document.getElementById("map"), {
            center: myLatLng,
            zoom: 6,
            });
        new google.maps.Marker({
        position: myLatLng,
        map,
        });
}}});