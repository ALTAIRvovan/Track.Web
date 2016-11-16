'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

var config = {
    bootstrapDir: "./node_modules/bootstrap-sass",
    bootstrapMaterialDir: "./node_modules/bootstrap-material-design"
};

gulp.task('sass', function () {
  return gulp.src('./assets/sass/**/*.scss')
    .pipe(sass({
      outputStyle: 'compressed',
      includePaths: [
          config.bootstrapDir + '/assets/stylesheets/',
          config.bootstrapMaterialDir + "/sass/"
      ]
    }).on('error', sass.logError))
    .pipe(gulp.dest('./static/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./assets/sass/**/*.scss', ['sass']);
});