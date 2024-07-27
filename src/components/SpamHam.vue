<template>
  <div class="container">
    <h2>Submit a sentence and we'll determine if it is spam or ham</h2>
    <SpamHamInput v-model="sentence" />
    <button @click="submitSentence">Submit</button>
    <div id="sentences" class="sentences">
      <div v-for="(item, index) in sentences" :key="index" :class="['sentence', item.sentimentClass]">
        {{ item.text }} - Sentiment: {{ item.sentiment }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import SpamHamInput from './SpamHamInput.vue';

const sentence = ref('');
const sentences = ref([]);

const submitSentence = async () => {
  console.log('Button clicked');
  if (sentence.value.trim()) {
    console.log('Sentence to be sent:', sentence.value);
    try {
      const response = await axios.post('https://render-0w2u.onrender.com/predict', {
        sentence: sentence.value,
      });
      console.log('Response received:', response);
      const sentimentClass = response.data.prediction === 'Ham' ? 'ham' : 'spam';
      const sentiment = response.data.prediction;
      sentences.value.push({ text: sentence.value, sentimentClass, sentiment });
      sentence.value = '';
    } catch (error) {
      console.error('Error:', error);
    }
  }
};
</script>

<style scoped>
.container {
  width: 100%;
  height: 400px;
  margin: auto;
  background-color: #ccc;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0);
}

.sentences {
  width: 100%;
  height: 100px;
  padding: 20px;
}

input[type="text"] {
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
  border-left-color: #4caf50;
}

.spam {
  border-left-color: #f44336;
}
</style>
