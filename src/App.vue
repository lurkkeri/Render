<script setup>
import SpamHamPredictor from './components/SpamHam.vue'

</script>

<template>
  <div id="app">
    <SpamHamPredictor />
  </div>
</template>

<script>
import SpamHamPredictor from './components/SpamHamPredictor.vue';

export default {
  name: 'App',
  components: {
    SpamHamPredictor
  }
};
</script>
<style>
body{
    padding: 20px;
    margin: 0;
    background-color:bisque;
}
.container {
    max-width: 600px;
    margin: auto;
    background-color: #ccc;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0);
}
input[type="text"]{
    width: calc(100% - 100px);
    padding: 10px;
    margin-right: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}
button {
    width: 90px;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
}
.sentence {
    border-left: 5px solid #ccc;
}
.ham {
    border-left-color: #4CAF50;
}
.spam{
    border-left-color: #F44336;
}
</style>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
