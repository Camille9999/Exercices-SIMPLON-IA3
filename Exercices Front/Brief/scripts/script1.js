const inputField = document.querySelector('#product-id');
const fetchButton = document.querySelector('#fetch-button');
const productImage = document.querySelector('#product-image');

fetchButton.addEventListener('click', () => {
  const productId = inputField.value;

  fetch(`https://world.openfoodfacts.org/api/v0/product/${productId}`)
    .then(response => response.json())
    .then(data => {
      const productImageUrl = data.product;

      productImage.src = productImageUrl.image_front_url;
    })
    .catch(error => {
      console.error(`Error fetching product data: ${error}`);
    });
});
