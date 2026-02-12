/**
 * Ice Cream Detailed Snippet
 * Plain vanilla JS — no framework dependencies.
 */
(function () {
    function renderBig(container, flavors) {
        container.innerHTML = "";
        if (!flavors || flavors.length === 0) {
            container.innerHTML =
                '<div class="text-center py-5">' +
                '<p class="text-muted fs-5">Momentálně nejsou k dispozici žádné příchutě.</p>' +
                '</div>';
            return;
        }
        flavors.forEach(function (flavor) {
            var wrapper = document.createElement("div");
            wrapper.className = "row mb-5 align-items-center s_icecream_detail_row";

            // Image column
            var imgCol = document.createElement("div");
            imgCol.className = "col-lg-6 mb-3 mb-lg-0";
            if (flavor.image_url) {
                var img = document.createElement("img");
                img.src = flavor.image_url;
                img.alt = flavor.name;
                img.className = "img-fluid rounded-4 shadow s_icecream_detail_img";
                img.loading = "lazy";
                imgCol.appendChild(img);
            } else {
                var ph = document.createElement("div");
                ph.className = "bg-light rounded-4 d-flex align-items-center justify-content-center";
                ph.style.minHeight = "250px";
                ph.innerHTML = '<i class="fa fa-image fa-3x text-muted"></i>';
                imgCol.appendChild(ph);
            }

            // Text column
            var textCol = document.createElement("div");
            textCol.className = "col-lg-6";

            var title = document.createElement("h3");
            title.textContent = flavor.name;
            textCol.appendChild(title);

            if (flavor.description) {
                var desc = document.createElement("div");
                desc.className = "lead";
                desc.innerHTML = flavor.description;
                textCol.appendChild(desc);
            }

            var hr = document.createElement("hr");
            textCol.appendChild(hr);

            var ingTitle = document.createElement("h5");
            ingTitle.innerHTML = '<i class="fa fa-list-ul me-2"></i>Složení';
            textCol.appendChild(ingTitle);

            var ingText = document.createElement("div");
            ingText.innerHTML = flavor.ingredients || "Složení není k dispozici.";
            textCol.appendChild(ingText);

            wrapper.appendChild(imgCol);
            wrapper.appendChild(textCol);
            container.appendChild(wrapper);
        });
    }

    function initBigSnippets() {
        var snippets = document.querySelectorAll(".s_icecream_big");
        snippets.forEach(function (el) {
            var container = el.querySelector(".s_icecream_content");
            if (!container) return;
            fetch("/icecream/featured")
                .then(function (r) { return r.json(); })
                .then(function (flavors) { renderBig(container, flavors); })
                .catch(function () {
                    container.innerHTML =
                        '<div class="text-center py-5">' +
                        '<p class="text-danger">Nepodařilo se načíst příchutě.</p>' +
                        '</div>';
                });
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initBigSnippets);
    } else {
        initBigSnippets();
    }
})();
