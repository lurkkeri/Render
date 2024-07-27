<template>
  <input :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" placeholder="Write your sentence" />
</template>

<script>
export default {
  name: 'SpamHamInput',
  props: {
    modelValue: {
      type: String,
      required: true
    }
  }
};
</script>
