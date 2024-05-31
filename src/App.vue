
<template>
  <div id="app">
    <SpamHam />
  </div>
</template>

<script>
import SpamHam from './components/SpamHam.vue';

export default {
  name: 'App',
  components: {
    SpamHam
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

