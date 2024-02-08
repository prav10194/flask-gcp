function getDescription() {
    console.log("Hello World");
    const element = document.querySelector("#descriptionId");

    // sending json
    const userData = { action: "search", product: document.getElementById("productInputId").value };

    axios
      .post("/productInfo", userData, {
        headers: { "Content-Type": "application/json" },
      })
      .then((response) => {
        // response is also json
        element.textContent = JSON.stringify(response.data, null, 4)
      });
}