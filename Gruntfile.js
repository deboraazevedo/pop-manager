module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    jshint: {
      dist: {
        src: [
              'core/static/assets/js/**/*.js',
             ]
      }
    },
    concat: {
      scripts: {
        src: [
              'core/static/assets/js/**/*.js',
             ],
        dest: 'core/static/dist/js/scripts.js',
      },
      libsjs: {
        src: [
              'core/static/bower_components/bootstrap/dist/js/bootstrap.js',
              'core/static/bower_components/metisMenu/dist/js/metisMenu.js',
              'core/static/bower_components/jquery/dist/jquery.js',
              'core/static/bower_components/raphael/raphael-min.js',
              'core/static/bower_components/morrisjs/morris.min.js',
              'core/static/bower_components/startbootstrap-sb-admin-2/dist/js/sb-admin-2.js'
             ],
        dest: 'core/static/dist/js/libs.js',
      }
    },
    uglify: {
      scripts: {
        src: [
              'core/static/dist/js/scripts.js'
             ],
        dest: 'core/static/dist/js/scripts.min.js'
      },
      libs: {
        src: [
              'core/static/dist/js/libs.js'
            ],
        dest: 'core/static/dist/js/libs.min.js'
      }
    },
    cssmin: {
      styles: {
        src: [
              'core/static/dist/css/style.css'
             ],
        dest: 'core/static/dist/css/style.min.css'
      },
      libs: {
        src: [
              'core/static/dist/css/libs.css'
             ],
        dest: 'core/static/dist/css/libs.min.css'
      }
    }
  });

  // Load the plugin's
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-clean');

  // Default task(s).
  grunt.registerTask('default', ['jshint', 'uglify', 'cssmin']);

};
