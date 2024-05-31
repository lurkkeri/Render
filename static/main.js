new Vue({
    el: '#app',
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
            const response = await axios.post('/predict', {
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
    },
    template: `
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
    `
  });
  