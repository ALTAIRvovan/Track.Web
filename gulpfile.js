'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');
var babel = require('gulp-babel');

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

gulp.task('scripts', function () {
    gulp.src(['./**/assets/js/*.js', '!./node_modules/**.js'])
        .pipe(sourcemaps.init())
        .pipe(babel({
            presets: ['es2015']
        }))
        .pipe(concat('all.js'))
        .pipe(uglify())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./static/js'))
        .pipe(gulp.dest('../collected_static/js'))
});

gulp.task('scripts:watch', function () {
    gulp.watch(['./**/assets/js/*.js', '!./node_modules/**.js'], ['scripts'])
});