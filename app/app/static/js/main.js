
    // get search from and page link
    let searchForm = document.getElementById("searchForm");
    let pageLinks = document.getElementsByClassName("page-link");

    // ensure searvh form exists
    if (searchForm) {
        for (let i = 0; pageLinks.length > i; i++) {
            pageLinks[i].addEventListener("click", function (e) {
                e.preventDefault();

                // get data attribute
                let page = this.dataset.page;
                // console.log("page: ", page);

                searchForm.innerHTML +=`<input value=${page} name="page" hidden />`

                searchForm.submit()
            });
        }
    }
