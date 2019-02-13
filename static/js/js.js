$(document).ready(function () {
    $("#profile-edit").click(function () {
        $(".profile-form").toggle();
    });
}); 


// QUICK SEARCH ON HOMEPAGE

let searchBar = document.getElementById("searchValue");

if (searchBar){
    const cardDisplay = document.querySelectorAll(".post-title");
    const pills = document.getElementById("Feature-tab");
    const displayBoxes = document.querySelectorAll(".display-wrapper");
    let searchBar = document.getElementById("searchValue").addEventListener("keyup", searchInput);
    let displaySearchResult = document.getElementById("search-matched");
    let list = document.getElementById("list-results")
    let spinner = document.querySelector(".fa-spinner");
    
    function searchInput(){
        let search = document.getElementById("searchValue").value.toUpperCase();
        count = 0;
        items = [];

        for(let i=0; i < cardDisplay.length; i++){
            let titles = cardDisplay[i].innerHTML.toUpperCase();

            if(titles.indexOf(search) > -1){
                displayBoxes[i].style.display = "";
                displaySearchResult.style.display = "";
                pills.classList.add("disabled")
                count += 1
                displaySearchResult.innerText = `${count} matches found!`
                items.push(displayBoxes[i])

            } else{
                displayBoxes[i].style.display = "none";
                pills.classList.add("disabled");
                displaySearchResult.style.display = "";
                displaySearchResult.innerText = `${count} matches found!`;
            } 
        }
        items.forEach(function(item){
            list.appendChild(item)
        })
        
        if(cardDisplay.length == count){
            count = 0;
            list.style.display = "none";
            displaySearchResult.style.display = "none";
            spinner.classList.add("fa-spinner-active");
            setTimeout(() => {
                location.reload()
            }, 1000);
        }
    }
} 

