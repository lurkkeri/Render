

<template>
  <div class="container">
    <h2>Submit a sentence and we'll determine if it is spam or ham</h2>
    <input type="text" v-model="sentence" placeholder="Write your sentence">
    <button @click="submitSentence">Submit</button>
    <div id="sentences" class="sentences">
      <div v-for="(item, index) in sentences" :key="index" :class="['sentence', item.sentimentClass]">
        {{ item.text }} - Sentiment: {{ item.sentiment }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
console.log("spamham");
export default {
  data() {
    return {
      sentence: '',
      sentences: []
    };
  },
  methods: {
    async submitSentence() {
    
      if (this.sentence.trim()) {
        try {
          const response = await axios.post('https://render-0w2u.onrender.com/predict', {
            sentence: this.sentence
          });
          const sentimentClass = response.data.prediction === 'Ham' ? 'ham' : 'spam';
          const sentiment = response.data.prediction;
          this.sentences.push({ text: this.sentence, sentimentClass, sentiment });
          this.sentence = '';
        } catch (error) {
          console.error('Error:', error);
        }
      }
    }
  }
};
</script>

  
<style scoped>
.container {
    width: 100%; /* Example: 100% width */
    height: 400px; 
    margin: auto;
    background-color: #ccc;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0);
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
    border-left-color: #4CAF50;
}
.spam {
    border-left-color: #F44336;
}
</style>
  