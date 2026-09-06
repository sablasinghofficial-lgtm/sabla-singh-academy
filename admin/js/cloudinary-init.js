
const CLOUD_NAME = "iqlwz76c";
const UPLOAD_PRESET = "ml_default";

window.openCloudinaryWidget = function(callback) {
    cloudinary.createUploadWidget({
        cloudName: CLOUD_NAME,
        uploadPreset: UPLOAD_PRESET,
        sources: ['local', 'url', 'camera'],
        multiple: false
    }, (error, result) => {
        if (!error && result && result.event === "success") {
            callback(result.info.secure_url);
        }
    }).open();
};
