let text_Area = document.getElementById("question");

const click_Button = document.getElementById('button');

click_Button.addEventListener("click", function(event){
    event.preventDefault();
    if (text_Area.value !== "Donnez moi le lieu qui vous interresse" && text_Area.value !== ""){
        fetch("/search?question="+text_Area.value)
            .then(function (response){
                    if (response.status !== 200) {
                        console.log('Erreur: ' + response.status);
                    return;
                    };
                    response.json().then(publish)
            });

    function publish(data) {
        const chat_elt = document.getElementById("papychat");
        const answer = document.getElementById("description");
        console.log(data.infos)
        let elt_to_publish = `<div class="container"><p class="font-weight-bold h-100">${text_Area.value.toUpperCase()}</p>
        <p class="answer_left">${data.pos_story}<br><br> Si tu veux en savoir plus,
        va voir sur <a href="https://fr.wikipedia.org/wiki/${text_Area.value}">Wikipedia</a></p>
        <p class="answer_left">Voici l'adresse: ${data.infos.address}</p>
        <div id="map" class="container" style="height: 350px;" ></div></div>`;
        answer.innerHTML = elt_to_publish;
        chat_elt.appendChild(answer);
        initMap(data)
        window.scrollBy(0, window.innerHeight);
        return data;
    };

    let map;
    function initMap(data) {
        console.log(document.getElementById("map"));
        const myLatLng = { lat: data.infos.lati, lng: data.infos.lngi };
        map = new google.maps.Map(document.getElementById("map"), {
            center: myLatLng,
            zoom: 4,
            });
        console.log(map);
        new google.maps.Marker({
        position: myLatLng,
        map,
        });
}}});