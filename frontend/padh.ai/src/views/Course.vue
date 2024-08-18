<template>
  <CourseProgAssignment v-if="progAssignmentQueryParam"></CourseProgAssignment>
  <CourseAssignment v-if="assignmentQueryParam"></CourseAssignment>
  <CourseMain v-if="!progAssignmentQueryParam && !assignmentQueryParam"></CourseMain>
</template>
<script>
import CourseMain from '@/components/CourseMain.vue';
import CourseAssignment from '@/components/CourseAssignment.vue';
import CourseProgAssignment from '@/components/CourseProgAssignment.vue';
export default {
  name: 'Course',
  components: {
    CourseMain,
    CourseAssignment,
    CourseProgAssignment,
  },
  data() {
    return {
      contentQueryParam: this.$route.query.contentId,
      assignmentQueryParam: this.$route.query.assignmentId,
      progAssignmentQueryParam: this.$route.query.progAssignmentId,
    }
  },
}
</script>
<style></style>
