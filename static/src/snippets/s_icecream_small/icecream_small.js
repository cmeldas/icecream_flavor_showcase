/**
 * Ice Cream Compact Snippet
 * Plain vanilla JS — no framework dependencies.
 */
(function () {
    function renderSmall(container, flavors) {
        container.innerHTML = "";
        if (!flavors || flavors.length === 0) {
            container.innerHTML =
                '<div class="col-12 text-center py-4">' +
                '<p class="text-muted fs-5">Momentálně nejsou k dispozici žádné příchutě.</p>' +
                '</div>';
            return;
        }
        var row = document.createElement("div");
        row.className = "row justify-content-center";
        flavors.forEach(function (flavor) {
            var col = document.createElement("div");
            col.className = "col-md-6 col-lg-5 mb-4";
            var card = document.createElement("div");
            card.className = "card h-100 shadow-sm s_icecream_card";
            if (flavor.image_url) {
                var img = document.createElement("img");
                img.src = flavor.image_url;
                img.alt = flavor.name;
                img.className = "card-img-top s_icecream_card_img";
                img.loading = "lazy";
                card.appendChild(img);
            }
            var body = document.createElement("div");
            body.className = "card-body";
            var title = document.createElement("h4");
            title.className = "card-title";
            title.textContent = flavor.name;
            body.appendChild(title);
            if (flavor.description) {
                var desc = document.createElement("div");
                desc.className = "card-text text-muted";
                desc.innerHTML = flavor.description;
                body.appendChild(desc);
            }
            card.appendChild(body);
            col.appendChild(card);
            row.appendChild(col);
        });
        container.appendChild(row);
    }

    function initSmallSnippets() {
        var snippets = document.querySelectorAll(".s_icecream_small");
        snippets.forEach(function (el) {
            var container = el.querySelector(".s_icecream_content");
            if (!container) return;
            fetch("/icecream/featured")
                .then(function (r) { return r.json(); })
                .then(function (flavors) { renderSmall(container, flavors); })
                .catch(function () {
                    container.innerHTML =
                        '<div class="col-12 text-center py-4">' +
                        '<p class="text-danger">Nepodařilo se načíst příchutě.</p>' +
                        '</div>';
                });
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initSmallSnippets);
    } else {
        initSmallSnippets();
    }
})();
