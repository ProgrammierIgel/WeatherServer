function add(city = "") {
  const value = prompt("Bitte gib den Ort ein, den du hinzufügen möchtest!");
  _api_post(value, "add").then(() => {
    window.location.href = window.location.href;
  });
}

function delete_entry(city) {
  _api_post(city, "delete").then(() => {
    window.location.reload();
  });
}

async function _api_post(value, arg) {
  return $.post("/wetter/", {
    data: value,
    arguments: arg,
  });
}
