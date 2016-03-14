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
              'core/static/bower_components/jquery/dist/jquery.js',
              'core/static/bower_components/bootstrap/dist/css/bootstrap.min.css'
             ],
        dest: 'core/static/dist/js/libs.js',
      },
      styles : {
        src: [
              'core/static/assets/css/*.css'
             ],
        dest: 'core/static/dist/css/style.css'
      },
      libscss: {
        src: [
              'core/static/bower_components/bootstrap/dist/css/bootstrap.css',
              'core/static/bower_components/bootstrap/dist/css/bootstrap-theme.css'
             ],
        dest: 'core/static/dist/css/libs.css'
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
              'core/static/bower_components/bootstrap/dist/js/bootstrap.js',
              'core/static/bower_components/jquery/dist/jquery.js'
            ],
        dest: 'core/static/dist/js/libs.min.js'
      }
    },
    cssmin: {
      styles: {
        src: [
              'core/static/dist/css/style.css',
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
  grunt.registerTask('default', ['jshint', 'concat', 'uglify', 'cssmin']);

};
